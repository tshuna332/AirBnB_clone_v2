#!/usr/bin/python3
"""asd a sdasd as d"""

from fabric.api import *
from datetime import datetime


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
