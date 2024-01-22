#!/usr/bin/env python3
"""
finds schools with a certain topic
"""


def schools_by_topic(mongo_collection,  topic):
    """
    returns the list of schools having a specific topic.
    """
    query = {"topics": topic}
    projection = {"_id": 1, "name": 1, "topics": 1}
    schools = mongo_collection.find(query, projection)
    return schools
