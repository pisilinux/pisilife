# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "wuala"

def install():
    pisitools.insinto("usr","usr/bin/")
    pisitools.insinto("usr","usr/lib/")
    pisitools.insinto("usr","usr/share/")