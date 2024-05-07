#!/usr/bin/python3
"""
clean outdated archives
"""
from fabric.api import *
import os


env.hosts = ['52.91.154.62', '54.166.175.242']
env.Key_file = "~/id_rsa"
env.user = 'ubuntu'


def do_clean(number=0):
    """
    delete outdated archives
    Args:
        number: the number of archive to keep
    """
    number = 1 if int(number) == 0 else int(number)
    archs = sorted(os.listdir("versions"))
    for i in range(number):
        archs.pop()
    with lcd("versions"):
        for arch in archs:
            local('rm ./{}'.format(arch))
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        for i in range(number):
            archive.pop()
        for arc in arcives:
            run('rm ./{}'.format(arc))
