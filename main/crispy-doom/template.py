pkgname = "crispy-doom"
pkgver = "7.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf"]
makedepends = [
    "libpng-devel",
    "libsamplerate-devel",
    "sdl2-compat-devel",
    "sdl2_mixer-devel",
    "sdl2_net-devel",
]
pkgdesc = "Limit-removing enhanced-resolution Doom source port"
license = "GPL-2.0-or-later"
url = "https://github.com/fabiangreffrath/crispy-doom"
source = f"{url}/archive/crispy-doom-{pkgver}.tar.gz"
sha256 = "25eea88fdbe1320ad0d1a3e0ed66ae8d985c39b79e442beab5fc36d9d5ddfc42"
hardening = ["vis", "!cfi", "!int"]

def post_install(self):
    # Remove all .desktop except the Doom one
    for f in [
        "usr/share/applications/*Heretic.desktop",
        "usr/share/applications/*Hexen.desktop",
        "usr/share/applications/*Strife.desktop",
    ]:
        self.uninstall(f, glob=True)

            