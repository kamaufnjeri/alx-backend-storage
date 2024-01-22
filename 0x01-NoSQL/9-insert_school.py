#!/usr/bin/env python3
""" insert into collection"""


def insert_school(mongo_collection, **kwargs):
    """
    insert a documents into coll3ction
    """
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id