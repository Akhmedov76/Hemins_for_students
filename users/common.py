import hashlib
from typing import Any

from month_4.lesson_3_hemins.home_task.file_manager import datas_manager

Admin_login = "admin"
Admin_password = "admin"


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_login = False

    def check_password(self, confirm_password):
        return confirm_password == self.password

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()


def login() -> dict[str, bool] | str | Any:
    try:
        username = input("Enter your login password: ").capitalize().strip()
        password = input("Enter your password: ").lower().strip()
        check_password = User.hash_password(password)
        read = datas_manager.read_json()
        if username == Admin_login.capitalize() and password == Admin_password.lower():
            return {'is_login': True, 'role': 'admin'}

        for user in read:
            if user["username"] == username and user["password"] == check_password:
                user["is_login"] = True
                datas_manager.write_json(read)
                print("Login successful!")
                if user['role'] == 'teacher':
                    return {'is_login': True, 'role': 'teacher'}
                elif user['role'] == 'student':
                    return {'is_login': True, 'role': 'student'}
                else:
                    return {'is_login': False, 'role': None}
        print("Login failed!")
        return {'is_login': False, 'role': None}
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return {'is_login': False, 'role': None}


def logout():
    try:
        txt = """
Are you sure you want to exit? Yes or No
        """
        print(txt)
        choice = (input("Enter your answer: ").lower())
        if choice == "yes":
            read = datas_manager.read_json()
            for user in read:
                user["is_login"] = False
                datas_manager.write_json(read)
            return True
    except Exception as e:
        print(f"An error occurred: {str(e)}")
