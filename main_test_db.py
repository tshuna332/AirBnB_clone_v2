#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.db_storage import DBStorage
from models.state import State

db = DBStorage()

# All States
all_states = db.all()
print(all_states)

