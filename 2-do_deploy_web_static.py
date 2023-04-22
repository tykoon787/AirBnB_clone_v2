#!/usr/bin/python3
# This script deploys an archieve of web_static to the servers

from fabric.api import run, env, put, local
from datetime import datetime
import os
# Hosts
web_01 = '54.160.79.52'
web_02 = '54.160.79.52'
env.user = 'ubuntu'
env.host = [web_01, web_02]


def do_pack():
    """Create a .tgz archive from web_static/"""
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(timestamp)
    local("tar -czvf {} web_static".format(filename))
    return filename


def do_deploy(archive_path):
    """Deploys the archive to the server"""
    if os.path.exists(archive_path):
        # Upload to /tmp/
        put(archive_path, "/tmp/")

        # Uncompress the archive
        dest = "/data/web_static/releases/"
        run("tar -xzvf {} -C {}".format(archive_path, dest))

        # Delete the archieve
        run("rm -f /tmp/{}".format(archive_path))

        # Delete symlink
        run("rm -f /data/web_static/current/test")

        # Creating new symlink
        basename = os.path.basename(archive_path)
        filename = os.path.splitext(basename)[0]
        run("ln -s /data/web_static/current {}".format(dest/filename))

        return True
    else:
        return False
