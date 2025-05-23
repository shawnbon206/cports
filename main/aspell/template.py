pkgname = "aspell"
pkgver = "0.60.8.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
]
pkgdesc = "Spell checker with good multi-language support"
license = "LGPL-2.1-only"
url = "http://aspell.net"
source = f"https://ftp.gnu.org/gnu/aspell/aspell-{pkgver}.tar.gz"
sha256 = "d6da12b34d42d457fa604e435ad484a74b2effcd120ff40acd6bb3fb2887d21b"


@subpackage("aspell-libs")
def _(self):
    return self.default_libs()


@subpackage("aspell-devel")
def _(self):
    return self.default_devel()
