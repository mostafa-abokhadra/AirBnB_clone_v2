#!/usr/bin/python3
"""full deploy"""

do_deploy = __import__('2-do_deploy_web_static').do_deploy
do_pack = __import__('1-pack_web_static').do_pack


def deploy():
    """full deploy"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
