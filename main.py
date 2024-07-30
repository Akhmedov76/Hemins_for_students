from users.admin import (create_subject, show_all_subjects, update_subject, delete_subject, add_teacher,
                         show_all_teachers, update_teacher, delete_teacher, creat_group, show_all_groups,
                         update_group, delete_group, add_student, show_all_students, update_student, delete_student,
                         manage_lessons, show_lessons, add_student_to_group)
from users.teacher import show_active_lessons, login_lessons, grading_students, ended_lessons, show_my_ended_lessons
from users.student import show_active_lesson, show_grade
from month_4.lesson_3_hemins.home_task.users.common import login, logout


def show_auth_menu():
    txt = """
1. Login 
2. Exit 
"""
    print(txt)
    user_input = input("Choose from menu: ")
    if user_input == "1":
        role = login()
        if not role['is_login']:
            show_auth_menu()
        elif role['role'] == "admin":
            admin_menu()
        elif role['role'] == "teacher":
            teacher_menu()
        elif role['role'] == "student":
            student_menu()
        else:
            print("Invalid credentials!")
            show_auth_menu()
    elif user_input == "2":
        if logout():
            print("Logout successful!")
        else:
            print("Logout canceled!")
            show_auth_menu()
    else:
        print("Invalid credentials!")
        show_auth_menu()


def admin_menu():
    txt = """
1. Teacher Management
2. Subject Management
3. Group Management
4. Student Management
5. Manage lessons -> group_name, teacher, time
6. Add students to the group
7. Show lessons table
8. Exit
    """
    print(txt)
    user_input = input("Choose from menu: ")
    if user_input == "1":
        teachers_menu()
    elif user_input == "2":
        subjects_menu()
    elif user_input == "3":
        groups_menu()
    elif user_input == "4":
        students_menu()
    elif user_input == "5":
        if manage_lessons():
            admin_menu()
        else:
            print("Error managing lessons!")
            admin_menu()
    elif user_input == "6":
        if add_student_to_group():
            admin_menu()
        else:
            print("Error adding student!")
            admin_menu()
    elif user_input == "7":
        if show_lessons():
            admin_menu()

    elif user_input == "8":
        print("Exit successful!")
        show_auth_menu()
    else:
        print("Invalid choice!")
        admin_menu()


def subjects_menu():
    txt = """
1. Create a new subject
2. Show all subjects
3. Update a subject
4. Delete a subject
5. Exit   
    """
    print(txt)
    user_input = input("Choose from menu: ")
    if user_input == "1":
        if create_subject():
            subjects_menu()
        else:
            print("Error creating subject!")
            subjects_menu()
    elif user_input == "2":
        if show_all_subjects():
            subjects_menu()
        else:
            print("Error showing subjects!")
            subjects_menu()
    elif user_input == "3":
        if update_subject():
            subjects_menu()
        else:
            print("Error updating subject!")
            subjects_menu()
    elif user_input == "4":
        if delete_subject():
            subjects_menu()
        else:
            print("Error deleting subject!")
            subjects_menu()
    elif user_input == "5":
        print("Exit successful!")
        admin_menu()
    else:
        print("Invalid choice!")
        subjects_menu()


def teachers_menu():
    txt = """
1. Create a new teacher
2. Show all teachers
3. Update a teacher information
4. Delete a teacher information
5. Exit
    """
    print(txt)
    user_input = input("Choose from menu: ")
    if user_input == "1":
        if add_teacher():
            teachers_menu()
        else:
            print("Error creating teacher!")
            teachers_menu()
    elif user_input == "2":
        if show_all_teachers():
            teachers_menu()
    elif user_input == "3":
        if update_teacher():
            teachers_menu()
        else:
            print("Error updating teacher!")
            teachers_menu()
    elif user_input == "4":
        if delete_teacher():
            teachers_menu()
        else:
            print("Error deleting teacher!")
            teachers_menu()
    elif user_input == "5":
        print("Exit successful!")
        admin_menu()
    else:
        print("Invalid choice!")
        teachers_menu()


def groups_menu():
    txt = """
1. Creat a new group
2. Show all groups
3. Update a group information
4. Delete a group information
5. Exit
    """
    print(txt)
    user_input = input("Choose from menu: ")
    if user_input == "1":
        if creat_group():
            groups_menu()
        else:
            print("Error creating group!")
            groups_menu()
    elif user_input == "2":
        if show_all_groups():
            groups_menu()
        else:
            print("Error updating group!")
            groups_menu()
    elif user_input == "3":
        if update_group():
            groups_menu()
        else:
            print("Error updating group!")
            groups_menu()
    elif user_input == "4":
        if delete_group():
            groups_menu()
        else:
            print("Error deleting group!")
            groups_menu()
    elif user_input == "5":
        print("Exit successful!")
        admin_menu()
    else:
        print("Invalid choice!")
        groups_menu()


def students_menu():
    txt = """
1. Create a new student
2. Show all students
3. Update a student information
4. Delete a student information
5. Exit
    """
    print(txt)
    user_input = input("Choose from menu: ")
    if user_input == "1":
        if add_student():
            students_menu()
        else:
            print("Error creating student!")
            students_menu()
    elif user_input == "2":
        if show_all_students():
            students_menu()
        else:
            print("Error showing students!")
            students_menu()
    elif user_input == "3":
        if update_student():
            students_menu()
        else:
            print("Error updating student!")
            students_menu()
    elif user_input == "4":
        if delete_student():
            students_menu()
        else:
            print("Error deleting student!")
            students_menu()
    elif user_input == "5":
        print("Exit successful!")
        admin_menu()
    else:
        print("Invalid choice!")
        students_menu()


def teacher_menu():
    txt = """
Welcome to teacher menu:
1. Show my active lessons
2. Start lesson:
3. Show my ended lessons
4. Exit
    """
    print(txt)
    user_input = input("Choose from menu: ")
    if user_input == "1":
        if show_active_lessons():
            teacher_menu()
        else:
            print("Error showing active lessons!")
            teacher_menu()
    elif user_input == "2":
        if login_lessons():
            teacher_lessons_menu()
        else:
            print("Error starting lesson!")
            teacher_menu()
    elif user_input == "3":
        if show_my_ended_lessons():
            teacher_menu()
        else:
            print("Error showing ended lessons!")
            teacher_menu()
    elif user_input == "4":
        print("Exit successful!")
        admin_menu()
    else:
        print("Invalid choice!")
        students_menu()


def teacher_lessons_menu():
    txt = """
1. Grading students
2. Ended lesson
    """
    print(txt)
    user_input = input("Choose from menu: ")
    if user_input == "1":
        if grading_students():
            teacher_lessons_menu()
        else:
            print("Error grading students!")
            teacher_lessons_menu()
    elif user_input == "2":
        if ended_lessons():
            teacher_menu()
        else:
            print("Error ending lesson!")
            teacher_lessons_menu()
    else:
        print("Invalid choice!")
        teacher_lessons_menu()


def student_menu():
    txt = """
Welcome to student menu:
1. Show my active lessons
2. Show my grade
3. Show my grade by subject
4. Exit
"""
    print(txt)
    user_input = input("Choose from menu: ")
    if user_input == "1":
        if show_active_lesson():
            student_menu()
        else:
            print("Error showing active lesson!")
            student_menu()
    elif user_input == "2":
        if show_grade():
            student_menu()
        else:
            print("Error showing grade!")
            student_menu()
    elif user_input == "3":
        pass
    elif user_input == "4":
        print("Exit successfull!")
        show_auth_menu()
    else:
        print("Invalid choice!")
        student_menu()


if __name__ == "__main__":
    show_auth_menu()
