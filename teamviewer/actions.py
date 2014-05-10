#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = ["/opt/teamviewer9/tv_bin/wine/drive_c/TeamViewer/tvwine.dll.so"]

def setup():
    shelltools.system("rpm2targz -v %s/teamviewer_linux.rpm" %get.workDIR())
    shelltools.system("tar xfvz %s/teamviewer_linux.tar.gz --exclude=var --exclude=etc --exclude=usr" %get.workDIR())
    
def install():
    pisitools.insinto("/opt/", "./opt/*")
    pisitools.remove("/opt/teamviewer9/tv_bin/xdg-utils/xdg-email")
    
    #necessary symlinks
    pisitools.dosym("/opt/teamviewer9/tv_bin/teamviewerd", "etc/init.d/teamviewerd")
    pisitools.dosym("/opt/teamviewer9/tv_bin/script/teamviewer", "usr/bin/teamviewer")
    pisitools.dosym("/opt/teamviewer9/logfiles", "var/log/teamviewer")
    pisitools.dosym("/opt/teamviewer9/config", "etc/teamviewer")
    
    pisitools.dodoc("%s/opt/teamviewer9/doc/License.txt" %get.workDIR())
    
    
    shelltools.chmod("%s/opt/teamviewer9/*" % get.installDIR(),0755)  
    
    
    
    