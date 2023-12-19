#!/usr/bin/env python3
"""
8-all mode
"""
from typing import List


def list_all(mongo_collection: Collection) -> List:
    """
    Lists all documents in a collection.
    """
    documents = list(mongo_collection.find())
    return documents