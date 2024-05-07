#!/usr/bin/python3
"""
A fabric file that packs the contents of web_static
folder into a .tgz file
"""


from fabric.api import local
import tarfile
import re
from datetime import datetime
import os.path


def do_pack():
    """
    packs a folder to .tgz
    """
    dest = local("mkdir -p versions")
    file_name = str(datetime.now()).replace(" ", "")
    options = re.sub(r'[^\w\s]', '', file_name)
    tar = local('tar -cvzf versions/web_static_{}.tgz'.format(options))
    if os.path.exists("./versions/web_static_{}.tgz".format(options)):
        return os.path.normpath("/versions/web_static_{}.tgz".format(options))
    else:
        return None
