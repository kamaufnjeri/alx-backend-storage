#!/usr/bin/env python3
""" list all documents with python"""


def list_all(mongo_collection):
    """ list all documents"""
    documents = mongo_collection.find()

    return documents