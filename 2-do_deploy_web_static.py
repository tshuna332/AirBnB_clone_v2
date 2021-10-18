#!/usr/bin/python3
"""asd a sdasd as d"""

from fabric.api import *
from datetime import datetime

env.hosts = ['35.196.90.236', '34.73.156.98']
env.user = "ubuntu"

def do_pack():
    """ADSFF ADSFASDFADSF"""
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if result.failed:
        return None
    return result


def do_deploy(archive_path):
    """SDFSDF DSFDSF DSFDS FDSSD F"""
    if not os.path.exists(archive_path):
        return False
    rex = r'^versions/(\S+).tgz'
    match = re.search(rex, archive_path)
    filename = match.group(1)
    res = put(archive_path, "/tmp/{}.tgz".format(filename))
    if res.failed:
        return False
    res = run("sudo mkdir -p /data/web_static/releases/{}/".format(filename))
    if res.failed:
        return False
    res = run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
              .format(filename, filename))
    if res.failed:
        return False
    res = run("sudo rm /tmp/{}.tgz".format(filename))
    if res.failed:
        return False
    res = run("sudo mv /data/web_static/releases/{}"
              "/web_static/* /data/web_static/releases/{}/"
              .format(filename, filename))
    if res.failed:
        return False
    res = run("sudo rm -rf /data/web_static/releases/{}/web_static"
              .format(filename))
    if res.failed:
        return False
    res = run("sudo rm -rf /data/web_static/current")
    if res.failed:
        return False
    res = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
              .format(filename))
    if res.failed:
        return False
    print('New version deployed!')
    return True
