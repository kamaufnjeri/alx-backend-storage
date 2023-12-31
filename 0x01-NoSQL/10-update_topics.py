#!/usr/bin/env python3
"""
10-update_topics mode
"""


def update_topics(mongo_collection, name,  topics):
    """
    Changes all topics of a school document based on the name.
    """
    query = {"name": name}
    update = {"$set": {"topics": topics}}
    result = mongo_collection.update_many(query, update)