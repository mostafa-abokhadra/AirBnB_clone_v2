#!/usr/bin/python3
"""making archeive
"""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
	"""making archeive
	"""
	try:
		local('mkdir -p versions')
		archive_path = 'versions/web_static_{}.tgz'.format(
		datetime.now().strftime('%Y%m%d%H%M%S'))
		local('tar -cvzf {} web_static'.format(archive_path))
		print('web_static packed: {} -> {}'.format(archive_path,
		os.path.getsize(archive_path)))
	except:
		return None
	
