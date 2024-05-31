#!/usr/bin/python3
# deploying
"""doplying finally"""

import os.path
from fabric.api import put, env, run

env.hosts = ["ubuntu@54.90.62.95", "ubuntu@54.90.37.231"]
env.user = "ubuntu"


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
