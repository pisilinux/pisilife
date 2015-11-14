#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "."
NoStrip = ["/"]

def setup():
    shelltools.system("rpm2targz -v %s/vivaldi-beta-1.0.303.52-2.x86_64.rpm" %get.workDIR())
    shelltools.system("tar xfvz %s/vivaldi-beta-1.0.303.52-2.x86_64.tar.gz --exclude=usr/bin --exclude=etc" %get.workDIR())
    shelltools.chmod(get.workDIR() + "/opt/vivaldi/*", 0755)

def install():
    pisitools.insinto("/opt/", "./opt/*")
    pisitools.insinto("/usr/", "./usr/*")
    shelltools.system("chmod -v 4755 %s/opt/vivaldi/vivaldi-sandbox" %get.installDIR())
    pisitools.dosym("/opt/vivaldi/vivaldi", "/usr/bin/vivaldi-preview")
    pisitools.dosym("/opt/vivaldi/product_logo_22.png", "/usr/share/icons/hicolor/22x22/apps/vivaldi.png")
    pisitools.dosym("/opt/vivaldi/product_logo_24.png", "/usr/share/icons/hicolor/24x24/apps/vivaldi.png")
    pisitools.dosym("/opt/vivaldi/product_logo_32.png", "/usr/share/icons/hicolor/32x32/apps/vivaldi.png")
    pisitools.dosym("/opt/vivaldi/product_logo_48.png", "/usr/share/icons/hicolor/48x48/apps/vivaldi.png")
    pisitools.dosym("/opt/vivaldi/product_logo_64.png", "/usr/share/icons/hicolor/64x64/apps/vivaldi.png")
    pisitools.dosym("/opt/vivaldi/product_logo_128.png", "/usr/share/icons/hicolor/128x128/apps/vivaldi.png")
    pisitools.dosym("/opt/vivaldi/product_logo_256.png", "/usr/share/icons/hicolor/256x256/apps/vivaldi.png")
    #pisitools.removeDir("/usr/share/xfce4")
