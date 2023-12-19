#!/usr/bin/env python3
"""
nginx_stats module
"""

from pymongo import MongoClient


def nginx_stats():
    """
    Provides some stats about Nginx logs stored in MongoDB
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the collection
    nginx_collection = client.logs.nginx

    # Get the total number of logs
    total_logs = nginx_collection.count_documents({})

    # Display total logs
    print(f"{total_logs} logs where {total_logs} is the number of documents in this collection")

    # Display methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod={method}: {count}")

    # Display specific log count
    status_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"\tmethod=GET path=/status: {status_count}")


if __name__ == "__main__":
    nginx_stats()
