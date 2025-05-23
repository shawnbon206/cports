pkgname = "libevdev"
pkgver = "1.13.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-gcov"]
hostmakedepends = ["pkgconf", "python", "automake", "libtool"]
makedepends = ["check-devel", "linux-headers"]
checkdepends = ["bash"]
pkgdesc = "Wrapper library for evdev devices"
license = "MIT"
url = "https://www.freedesktop.org/wiki/Software/libevdev"
source = f"$(FREEDESKTOP_SITE)/libevdev/libevdev-{pkgver}.tar.xz"
sha256 = "f00ab8d42ad8b905296fab67e13b871f1a424839331516642100f82ad88127cd"
# FIXME int
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libevdev-devel")
def _(self):
    self.depends += ["linux-headers"]
    return self.default_devel()


@subpackage("libevdev-progs")
def _(self):
    return self.default_progs()
