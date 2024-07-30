from month_4.lesson_3_hemins.home_task.file_manager import (datas_manager, subject_manager,
                                                            group_manager)
import random
import hashlib
from datetime import datetime


class Subject:
    def __init__(self, subject_id, subject_name, subject_author, create_date):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.subject_author = subject_author
        self.create_date = create_date


# This function for create a new subject
def create_subject():
    try:
        subject_id = random.randint(1, 100)
        subject_name = input("Enter the name of the subject: ").capitalize()
        subject_author = input("Enter the author of the subject: ").capitalize()
        create_subject_data = str(datetime.now().strftime('%Y-%m-%d %H:%M`'))
        subject = Subject(subject_id, subject_name, subject_author, create_subject_data)
        subject_manager.add_to_file(subject.__dict__)
        print("Subject created successfully.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


# This function is show all the information about the subject
def show_all_subjects():
    try:
        data = subject_manager.read_json()
        if data:
            for subject in data:
                print(f"Subject ID: {subject['subject_id']}")
                print(f"Subject Name: {subject['subject_name']}")
                print(f"Subject Author: {subject['subject_author']}")
                print(f"Created Date: {subject['create_date']}")
        else:
            print("No subjects found.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")


# This function is for updating a subject by name and teacher name
def update_subject():
    try:
        data = subject_manager.read_json()
        subject_name = input("Enter the name of the subject to update: ").capitalize()
        if data:
            for subject in data:
                if subject['subject_name'] == subject_name:
                    updated_sub_id = input("Enter the new id of the subject: ").capitalize()
                    updated_sub_name = input("Enter the new name of the subject: ").capitalize()
                    updated_sub_author = input("Enter the new author of the subject: ").capitalize()
                    updated_sub_data = str(datetime.now().strftime('%Y-%m-%d %H:%M`'))
                    updated_sub = Subject(updated_sub_id, updated_sub_name, updated_sub_author, updated_sub_data)
                    subject_manager.write_json(updated_sub.__dict__)
                    print("Subject updated successfully.")
                    return True
                else:
                    print("Subject not found.")
                    return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


# This function is for deleting a subject by name
def delete_subject():
    try:
        data = subject_manager.read_json()
        subject_name = input("Enter the name of the subject to delete: ").capitalize()
        if data:
            for subject in data:
                if subject['subject_name'] == subject_name:
                    data.remove(subject)
                    subject_manager.write_json(data)
                    print("Subject deleted successfully.")
                    return True
            else:
                print("Subject not found.")
                return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


class Teacher:
    def __init__(self, user_id, username, password, role, create_date):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role
        self.create_date = create_date
        self.is_login = False


# This feature is for adding a teacher
def add_teacher():
    try:
        user_id = random.randint(1, 100)
        teacher_name = input("Enter the name of the teacher: ").capitalize()
        teacher_password = hashlib.sha256((input("Enter your password: ")).encode()).hexdigest()
        role = input("Enter the role: ").lower()
        create_date = str(datetime.now().strftime('%Y-%m-%d %H:%M`'))
        teacher = Teacher(user_id, teacher_name, teacher_password, role, create_date)
        datas_manager.add_to_file(teacher.__dict__)
        print("Teacher added successfully.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def show_all_teachers():
    try:
        teachers = datas_manager.read_json()
        if teachers:
            print("Teachers:")
            for teacher in teachers:
                if teacher['role'] == "teacher":
                    print(
                        f"ID: {teacher['user_id']},\nUsername: {teacher['username']},\n"
                        f"Role: {teacher['role']}\nCreate_data: {teacher['create_date']}\n")
        else:
            print("No teachers found.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def update_teacher():
    try:
        teacher_name = input("Enter the name teacher you want to update: ").capitalize()
        updated_teacher_name = input("Enter the updated name teacher: ").capitalize()
        updated_date = str(datetime.now().strftime('%Y-%m-%d %H:%M`'))
        txt = """
        Choose the field you want to update:
        1. Update the name
        2. Update the password
        """
        print(txt)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            teachers = datas_manager.read_json()
            if teachers:
                for teacher in teachers:
                    if teacher["username"] == teacher_name:
                        teacher["username"] = updated_teacher_name
                        teacher["create_data"] = updated_date
                        datas_manager.write_json(teachers)
                        print("Teacher updated successfully.")
                        return True
                print("Teacher not found.")
            else:
                print("No teachers found.")
            return True
        elif choice == 2:
            teachers = datas_manager.read_json()
            if teachers:
                for teacher in teachers:
                    if teacher["username"] == teacher_name:
                        updated_teacher_password = hashlib.sha256(
                            (input("Enter the updated password: ")).encode()).hexdigest()
                        teacher["password"] = updated_teacher_password
                        datas_manager.write_json(teachers)
                        print("Teacher updated successfully.")
                        return True
                print("Teacher not found.")
                return True
            else:
                print("No teachers found.")
                return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def delete_teacher():
    try:
        teacher_name = input("Enter the name teacher you want to delete: ").capitalize()
        teachers = datas_manager.read_json()
        if teachers:
            for teacher in teachers:
                print(teacher)
                if teacher["username"] == teacher_name:
                    teachers.remove(teacher)
                    datas_manager.write_json(teachers)
                    print("Teacher deleted successfully.")
                    return True
            print("Teacher not found.")
        else:
            print("No teachers found.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


class Groups:
    def __init__(self, id, group_name, group_count, create_date):
        self.id = id
        self.group_name = group_name
        self.group_count = group_count
        self.create_date = create_date
        self.manage = []
        self.students = []


def creat_group():
    try:
        group_id = random.randint(1, 100)
        group_name = input("Enter the name of the group: ").capitalize()
        group_count = input("Number of groups: ")
        create_date = str(datetime.now().strftime('%Y-%m-%d %H:%M`'))
        group = Groups(group_id, group_name, group_count, create_date)
        group_manager.add_to_file(group.__dict__)
        print("Group added successfully.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def show_all_groups():
    try:
        groups = group_manager.read_json()
        if groups:
            print("Groups:")
            for group in groups:
                print(
                    f"ID: {group['id']},\nGroup_name: {group['group_name']},\n"
                    f"Group_count: {group['group_count']},\nCreate_data: {group['create_date']}\n")
        else:
            print("No groups found.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def update_group():
    try:
        group_name = input("Enter the name of the group you want to update: ").capitalize()
        updated_group_name = input("Enter the updated name of the group: ").capitalize()
        updated_group_count = input("Enter the updated number of groups: ")
        txt = """
        Choose the field you want to update:
        1. Update the group name
        2. Update the group count
        """
        print(txt)
        choice = int(input("Enter your choice: "))
        if choice == 1:
            groups = group_manager.read_json()
            if groups:
                for group in groups:
                    if group["group_name"] == group_name:
                        group["group_name"] = updated_group_name
                        group_manager.write_json(groups)
                        print("Group updated successfully.")
                        return True
                print("Group not found.")
            else:
                print("No groups found.")
            return True
        elif choice == 2:
            groups = group_manager.read_json()
            if groups:
                for group in groups:
                    if group["group_name"] == group_name:
                        group["group_count"] = updated_group_count
                        group_manager.write_json(groups)
                        print("Group updated successfully.")
                        return True
                print("Group not found.")
            else:
                print("No groups found.")
            return True
        else:
            print("Invalid choice.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def delete_group():
    try:
        group_name = input("Enter the name of the group you want to delete: ").capitalize()
        groups = group_manager.read_json()
        if groups:
            for group in groups:
                if group["group_name"] == group_name:
                    groups.remove(group)
                    group_manager.write_json(groups)
                    print("Group deleted successfully.")
                    return True
            print("Group not found.")
        else:
            print("No groups found.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


class Student:
    def __init__(self, user_id, username, password, role, create_date):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role
        self.create_date = create_date
        self.is_login = False

    # This feature is for adding a student


def add_student():
    try:
        student_id = random.randint(1, 100)
        username = input("Enter the username: ").capitalize()
        if username == "":
            print("Username cannot be empty.")
            return False
        password = hashlib.sha256((input("Enter the password: ")).encode()).hexdigest()
        if password == "":
            print("Password cannot be empty.")
            return False
        role = input("Enter the role: ").lower()
        create_date = str(datetime.now().strftime('%Y-%m-%d %H:%M`'))
        student = Student(student_id, username, password, role, create_date)
        datas_manager.add_to_file(student.__dict__)
        print("Student added successfully.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


# This feature is for displaying all students

def show_all_students():
    try:
        students = datas_manager.read_json()
        if students:
            print("Students:")
            for student in students:
                if student['role'] == 'student':
                    print(
                        f"Student_id: {student['user_id']}\nUsername: {student['username']},\n"
                        f"Password: {student['password']},\nRole= {student['role']},\nCreated_date: "
                        f"{student['create_date']},\n")
        else:
            print("No students found.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


# This feature is for updating a student

def update_student():
    try:
        username = input("Enter the username of the student you want to update: ").lower()
        password = input("Enter the password of the student you want to update: ")
        updated_username = input("Enter the updated username: ").lower()
        updated_password = hashlib.sha256((input("Enter the updated password: ")).encode()).hexdigest()
        updated_role = input("Enter the updated role: ").lower()
        created_date = str(datetime.now().strftime('%Y-%m-%d %H:%M`'))
        students = datas_manager.read_json()
        if students:
            for student in students:
                if student["username"] == username and student["password"] == password:
                    student["username"] = updated_username
                    student["password"] = updated_password
                    student["role"] = updated_role
                    student["create_date"] = created_date
                    datas_manager.write_json(students)
                    print("Student updated successfully.")
                    return True
                else:
                    print("Student not found.")
                    return False
        else:
            print("No students found.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


# This feature is for deleting a student

def delete_student():
    try:
        student_name = input("Enter the name student you want to delete: ").capitalize()
        students = datas_manager.read_json()
        if students:
            for teacher in students:
                if teacher["username"] == student_name:
                    students.remove(teacher)
                    datas_manager.write_json(students)
                    print("Student deleted successfully.")
                    return True
            print("Teacher not found.")
        else:
            print("No teachers found.")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def manage_lessons():
    data = datas_manager.read_json()
    groups = group_manager.read_json()
    subjects = subject_manager.read_json()

    teacher_id = int(input("Enter teacher ID: "))
    teacher_name = input("Enter teacher name: ").capitalize()
    group_name = input("Enter group name: ").capitalize()
    subject_name = input("Enter subject name: ").capitalize()

    teacher_found = False
    group_found = False
    subject_found = False

    for teacher in data:
        if teacher['username'] == teacher_name and teacher['role'] == 'teacher':
            teacher_found = True
            break

    if not teacher_found:
        print("Teacher not found.")
        return False

    for group in groups:
        if group['group_name'] == group_name:
            group_found = True
            break

    if not group_found:
        print("Group not found.")
        return False

    for subject_item in subjects:
        if subject_item['subject_name'] == subject_name:
            subject_found = True
            break

    if not subject_found:
        print("Subject not found.")
        return False

    new_data = {
        'teacher_id': teacher_id,
        'teacher_name': teacher_name,
        'group_name': group_name,
        'lesson': subject_name,
        "created_at": str(datetime.now().strftime('%Y-%m-%d %H:%M`')),
        "is_active": False
    }

    for group in groups:
        if group['group_name'] == group_name:
            group['manage'].append(new_data)
            group_manager.write_json(groups)

    print("Lesson managed successfully.")
    return True


def add_student_to_group():
    groups = group_manager.read_json()
    students = datas_manager.read_json()

    if not groups or not students:
        print("No groups or students found.")
        return False

    student_id = int(input("Enter student ID: "))
    group_name = input("Enter group name: ").capitalize()
    student_name = input("Enter student name: ").capitalize()

    group_found = False
    student_found = False

    for group in groups:
        if group['group_name'] == group_name:
            group_found = True
            break

    if not group_found:
        print("Group not found.")
        return False

    for student in students:
        if student['username'] == student_name and student['role'] == 'student' and student['user_id'] == student_id:
            student_found = True
            break

    if not student_found:
        print("Student not found.")
        return False

    all_students = {
        'student_id': student_id,
        'student_name': student_name,
        'time_joined_group': str(datetime.now().strftime('%Y-%m-%d %H:%M`'))
    }
    for group in groups:
        print(group)
        if group['group_name'] == group_name:
            group['students'].append(all_students)
            group_manager.write_json(groups)
            print("Student added to group successfully.")
            return True
        else:
            print("Group not found.")
            return False


def show_lessons():
    groups = group_manager.read_json()

    if not groups:
        print("No groups found.")
        return False

    for group in groups:
        for lesson in group['manage']:
            print(f"Teacher ID: {lesson['teacher_id']}")
            print(f"Teacher: {lesson['teacher_name']}")
            print(f"Subject: {lesson['lesson']}")
            print(f"Created at: {lesson['created_at']}")
            print("-" * 50)

    return True
