import os
import json


class JsonManager:
    def __init__(self, filename):
        self.file_name = filename

    # Check if the file exists and is not empty
    def check_file_exists(self):
        return os.path.exists(self.file_name)

    def read_json(self):
        if self.check_file_exists():
            if os.path.getsize(self.file_name) != 0:
                with open(self.file_name, "r") as file:
                    return json.load(file)
            return []  # Return empty list if file exists but empty
        return []  # Return empty list if file does not exist

    def write_json(self, data):
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)
            return "Data added successfully"

    # Add new data to the JSON file
    def add_to_file(self, data):
        items = self.read_json()  # Read existing data
        items.append(data)  # Append new data
        self.write_json(items)  # Write updated data to file
        return "Data added successfully"  # Confirmation message


# JsonManager for handling JSON files
datas_manager = JsonManager('./datas/data.json')
subject_manager = JsonManager('./datas/subject.json')
group_manager = JsonManager('./datas/group.json')
lessons_manager = JsonManager('./datas/lessons.json')
