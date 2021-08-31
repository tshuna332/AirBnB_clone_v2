#!/usr/bin/python3
"""asd a sdasd as d"""

from fabric.api import *
from datetime import datetime

env.hosts = ['35.196.90.236', '34.73.156.98']
env.user = "ubuntu"

def do_pack():
    """asd asd as d"""
    try:
        local('mkdir -p versions')
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        name = "versions/web_static_" + date + ".tgz"
        tar = local("tar -cvzf " + name + " web_static")
        return (name)
    except:
        return (None)

def do_deploy(archive_path):
    '''Deploy the tgz file in the server'''
    if (not archive_path):
        return (False)

     try:
        put(archive_path, '/tmp')
        folder = "/data/web_static/releases/" + archive_path[9:-4] + "/"
        run('mkdir -p ' + folder)
        run('tar -zxvf /tmp/' + archive_path[9:] + ' -C ' + folder)
        run('rm /tmp/' + archive_path[9:])
        run('rm -rf /data/web_static/current')
	run('ln -sf ' + folder + ' /data/web_static/current')
        run('mv ' + folder_path + "web_static/* " + folder_path)
        run('rm -rf ' + folder_path + 'web_static')
        return (True)
     except:
        return (False)
