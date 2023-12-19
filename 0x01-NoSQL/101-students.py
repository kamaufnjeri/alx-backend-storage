#!/usr/bin/env python3
"""pymongo"""


def top_students(collection):
    """
    Use aggregation to calculate the average score for
    each student and sort them in descending order.
    # The result includes only the 'name' and 'averageScore' fields.
    """
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