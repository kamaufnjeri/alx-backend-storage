#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def top_students(collection):
    """
    Returns all students sorted by average score.
    
    :param collection: pymongo collection object
    :return: MongoDB cursor with students sorted by average score
    """
    # Use aggregation to calculate the average score for each student and sort them in descending order.
    # The result includes only the 'name' and 'averageScore' fields.
    aggregation_pipeline = [
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]

    # Execute the aggregation pipeline
    sorted_students_cursor = collection.aggregate(aggregation_pipeline)

    return sorted_students_cursor


