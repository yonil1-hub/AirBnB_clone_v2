#!/usr/bin/python3
"""This pyhton script compresses the contents of webstatic to .tzg file"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """A method that acomplishes the above objective"""
    now = datetime.now()
    appended_name = now.strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_" + appended_name + ".tgz"

    local("mkdir -p versions")

    if local("tar -cvzf {} web_static".format(archive_name)).failed is True:
        return None

    return archive_name
