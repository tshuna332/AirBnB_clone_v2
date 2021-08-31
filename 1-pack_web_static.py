#!/usr/bin/python3
"""asd a sdasd as d"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """asd asd as d"""
    try:
        local('mkdir versions')
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        name = "web_static_" + date + ".tgz"
        tar = local("tar -cvzf versions/" + name + " web_static")
        return ("versions/" + name)
    except:
        return (None)
