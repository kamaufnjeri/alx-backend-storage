#!/usr/bin/env python3
"""top students"""


def top_students(mongo_collection):
    """top students"""
    students = mongo_collection.find()

    for student in students:
        total_score = 0
        num_topics = 0

        for topic in student.get('topics', []):
            total_score += topic.get('score', 0)
            num_topics += 1

        if num_topics > 0:
            average_score = total_score / num_topics
            student['averageScore'] = round(average_score, 2)
        else:
            student['averageScore'] = 0

    # Sorting students by averageScore in descending order
    sorted_students = sorted(students, key=lambda x: x['averageScore'], reverse=True)

    return sorted_students

# Rest of the code remains unchanged

