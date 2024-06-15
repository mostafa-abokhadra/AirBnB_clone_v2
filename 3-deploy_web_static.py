#!/usr/bin/python3
"""full deploy"""

import os.path
from fabric.api import put, env, run, local
from datetime import datetime

do_deploy = __import__('2-do_deploy_web_static').do_deploy
do_pack = __import__('1-pack_web_static').do_pack

env.hosts = ["ubuntu@54.90.62.95", "ubuntu@54.90.37.231"]
env.user = "ubuntu"

def deploy():
    """full deploy"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
