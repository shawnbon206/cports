pkgname = "cargo-c"
pkgver = "0.10.11"
pkgrel = 0
build_style = "cargo"
# no tests in others
make_check_args = ["--lib"]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "curl-devel",
    "libgit2-devel",
    "openssl3-devel",
    "rust-std",
    "sqlite-devel",
]
pkgdesc = "Cargo plugin to install C-ABI libraries"
license = "MIT"
url = "https://github.com/lu-zero/cargo-c"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    "https://github.com/rust-lang/git2-rs/archive/refs/tags/git2-0.20.0.tar.gz",
    f"!{url}/releases/download/v{pkgver}/Cargo.lock>Cargo.lock.{pkgver}",
]
source_paths = [".", "git2", "."]
sha256 = [
    "8a6d6dc589d6d70bd7eb95971e3c608240e1f9c938dd5b54a049977333b59f05",
    "d4b8b2b2526944d6cb75ecf8bcc2c1757fc1fa6deef94b6d32410b1f84f38d1b",
    "c65ee1fcd2fefa0a3c572477243c64326f21ff5c85b960a7975663141121eb91",
]
# mfs be like rebuild literally everything and then run
# test_semver_one_zero_zero and test_semver_zero_zero_zero
options = ["!check"]


def post_extract(self):
    self.cp(self.sources_path / f"Cargo.lock.{pkgver}", "Cargo.lock")


def post_prepare(self):
    from cbuild.util import cargo

    # nuke lockfiles that may still hold the old ver
    self.rm("vendor/cargo/Cargo.lock")
    self.rm("vendor/gix/Cargo.lock")

    cargo.clear_vendor_checksums(self, "cargo")
    cargo.clear_vendor_checksums(self, "gix")

    self.mv("git2/libgit2-sys", ".")
    self.mv("git2/git2-curl", ".")

    # nuke the old git2 stuff and replace with new
    for crt in ["libgit2-sys", "git2-curl", "git2"]:
        self.rm(f"vendor/{crt}", recursive=True)
        self.mv(crt, "vendor")

    # write updated checksums from lockfile
    cargo.write_vendor_checksum(
        self,
        "libgit2-sys",
        "e1a117465e7e1597e8febea8bb0c410f1c7fb93b1e1cddf34363f8390367ffec",
    )
    cargo.write_vendor_checksum(
        self,
        "git2-curl",
        "be8dcabbc09ece4d30a9aa983d5804203b7e2f8054a171f792deff59b56d31fa",
    )
    cargo.write_vendor_checksum(
        self,
        "git2",
        "3fda788993cc341f69012feba8bf45c0ba4f3291fcc08e214b4d5a7332d88aff",
    )


def post_install(self):
    self.install_license("LICENSE")
