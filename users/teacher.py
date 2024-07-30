from datetime import datetime

from month_4.lesson_3_hemins.home_task.file_manager import (group_manager, lessons_manager)


class Teacher:
    def __init__(self, lesson_id, student_id):
        self.lesson_id = lesson_id
        self.student_id = student_id

    # @staticmethod
    # def check_lesson_id(lesson_id):
    #     data = subject_manager.read_json()
    #     for lesson in data:
    #         if lesson["lesson_id"] == lesson_id:
    #             return True
    #     return False
    #
    # @staticmethod
    # def check_student_id(student_id):
    #     data = datas_manager.read_json()
    #     for student in data:
    #         if student["subject_id"] == student_id:
    #             return True
    #     return False


def show_active_lessons():
    data = group_manager.read_json()
    group_id = int(input("Enter the group ID: "))
    for group in data:
        if group['id'] == group_id:
            print("Active lessons:")
            for student in group['students']:
                print(
                    f"Student ID: {student['student_id']},\nStudent name: {student['student_name']},\n"
                    f"Student joined group: {student['time_joined_group']}")
            return True
    print("Group not found.")
    return False


def login_lessons():
    try:
        data = group_manager.read_json()
        group_id = int(input("Enter the group ID: "))
        for group in data:
            if group['id'] == group_id:
                student_id = group['students'][0]['student_id']
                print("Lesson started!")
                lesson_data = {
                    "group_id": group_id,
                    "student_id": student_id,
                    "grade": None,
                    "time_started": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                    "time_ended": None,
                    "status": "active"
                }
                lessons_manager.add_to_file(lesson_data)
                return True
        print("Group not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def grading_students():
    try:
        data = lessons_manager.read_json()
        group_id = int(input("Enter the group ID: "))
        for lesson in data:
            if lesson['group_id'] == group_id and lesson['status'] == "active":
                student_id = int(input("Enter the student ID: "))
                if lesson['student_id'] == student_id:
                    grade = int(input("Enter the grade: "))
                    lesson['grade'] = grade
                    lesson['time_ended'] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    lesson['status'] = "ended"
                    lessons_manager.write_json(data)
                    print("Grade updated successfully!")
                    return True
                print("Student not found.")
                return False
        print("Lesson not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def ended_lessons():
    data = lessons_manager.read_json()
    for lesson in data:
        if lesson['status'] == "active":
            lesson['status'] = "ended"
            lesson['time_ended'] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            lessons_manager.write_json(data)
            print("Lesson successfully ended!")
    return True


def show_my_ended_lessons():
    data = lessons_manager.read_json()
    for lesson in data:
        if lesson['status'] == "ended":
            print(
                f"Group ID: {lesson['group_id']},\nStudent ID: {lesson['student_id']},\nGrade: {lesson['grade']},"
                f"\nTime started: {lesson['time_started']},\nTime ended: {lesson['time_ended']}")
    return True
