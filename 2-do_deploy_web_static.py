#!/usr/bin/python3
"""
upload and setup
"""
from fabric.api import *
import os

env.hosts = ['52.91.154.62', '54.166.175.242']
env.Key_file = "~/id_rsa"
env.user = 'ubuntu'


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
