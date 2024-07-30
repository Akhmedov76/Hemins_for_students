"""
Student menu:
    1. Show my active lessons
    2. Show my grade
    3. Show my grade by subject
    4. Logout
"""
from datetime import datetime

from month_4.lesson_3_hemins.home_task.file_manager import group_manager, lessons_manager


class Student:
    def __init__(self, name):
        self.name = name


def show_active_lesson():
    data = group_manager.read_json()
    group_id = int(input("Enter the group ID: "))
    for group in data:
        if group['id'] == group_id:
            print("Active lessons:")
            for student in group['students']:
                print(
                    f"Student ID: {student['student_id']},\nName: {student['student_name']},\n Time joined:"
                    f"{student['time_joined_group']}\n")
                return True
        return False

    print("Group not found.")
    return False


def show_grade():
    lessons = lessons_manager.read_json()
    group_id = int(input("Enter the group ID: "))
    for lesson in lessons:
        if lesson['group_id'] == group_id:
            print(f"Grade for {lesson['subject']}: {lesson['grade']}")
            return True
        return False
    print("Lesson not found.")
    return False


def show_grade_by_subject():
    lessons = lessons_manager.read_json()
    group_id = int(input("Enter the group ID: "))
    pass
