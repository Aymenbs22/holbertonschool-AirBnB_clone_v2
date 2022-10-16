#!/usr/bin/python3
"""
Fabric script that generates a .tgz
archive from the contents of the web_static
folder of your AirBnB Clone repo
using the function do_pack
"""

from os.path import isdir
from datetime import datetime
from fabric.api import local


def do_pack():
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        flname = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(flname))
    except:
        return None
