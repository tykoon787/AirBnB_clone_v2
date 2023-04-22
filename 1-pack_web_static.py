#!/usr/bin/env python3
# This is a Fabric Script that creates a .tgz from the webstatic
# Folder

from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a .tgz archive from web_static/"""
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(timestamp)
    local("tar -czvf {} web_static".format(filename))
    return filename
