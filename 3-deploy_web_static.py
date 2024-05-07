#!/usr/bin/python3
"""
pack, upload and deploy
"""
from fabric.api import *
import os
from datetime import datetime
import tarfile
import re


env.hosts = ['52.91.154.62', '54.166.175.242']
env.Key_file = "~/id_rsa"
env.user = 'ubuntu'


def do_pack():
    """
    packs a folder to .tgz
    """
    dest = local("mkdir -p versions")
    file_name = str(datetime.now()).replace(" ", "")
    fn = re.sub(r'[^\w\s]', '', file_name)
    tar = local('tar -cvzf versions/web_static_{}.tgz web_static'.format(fn))
    if os.path.exists("./versions/web_static_{}.tgz".format(fn)):
        return os.path.normpath("/versions/web_static_{}.tgz".format(fn))
    else:
        return None


def do_deploy(archive_path):
    """
    distribute to the server
    """
    if os.path.exists(archive_path) is False:
        return False
    try:
        archive = archive_path.split("/")
        wotgz = archive[1].strip('.tgz')
        put(archive_path, '/tmp/')
        sudo('mkdir -p /data/web_static/releases/{}'.format(wotgz))
        path = '/data/web_static/releases/{}'.format(wotgz)
        sudo('tar -xzf /tmp/{} -C {}/'.format(archive[1], path))
        sudo('rm /tmp/{}'.format(archive[1]))
        sudo('mv {}/web_static/* {}/'.format(path, path))
        sudo('rm -rf /data/web_static/current')
        sudo('ln -s {}/ "/data/web_static/current"'.format(path))
        return True
    except Exception:
        return False


def deploy():
    """
    packs and deploys
    """
    path = do_pack()
    if path is None:
        return False
    deployed = do_deploy(path)
    return deployed
