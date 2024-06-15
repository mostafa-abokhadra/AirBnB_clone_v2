#!/usr/bin/python3
"""full deploy"""

from fabric.api import local, put, env, run
from datetime import datetime
import os.path

env.hosts = ["ubuntu@54.90.62.95", "ubuntu@54.90.37.231"]
env.user = "ubuntu"


def do_pack():
    """making archeive"""
    try:
        local('mkdir -p versions')
        archive_path = 'versions/web_static_{}.tgz'.format(
                    datetime.now().strftime('%Y%m%d%H%M%S'))
        local('tar -cvzf {} web_static'.format(archive_path))
        print('web_static packed: {} -> {}'.format(
                archive_path, os.path.getsize(archive_path)))
        return archive_path
    except Exception:
        return No


def do_deploy(archive_path):
    """deploying to server
    """
    if os.path.exists(archive_path):
        file_name = archive_path.split('/')[-1]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}".format(
            file_name.split('.')[0]))
        run("tar -xf /tmp/{}  -C /data/web_static/releases/{}".format(
            file_name, file_name.split('.')[0]))

        run("rm /tmp/{}".format(file_name))
        run("mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".format(
            file_name.split('.')[0], file_name.split('.')[0]))
        run("rm -rf /data/web_static/releases/{}/web_static".format(
            file_name.split('.')[0]))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{} \
                /data/web_static/current".format(
            file_name.split('.')[0]))
        print("New version deployed!")
        return True
    else:
        return False


def deploy():
    """full deploy"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
