from pymongo import MongoClient
from datetime import datetime


class AttendanceManager:

    def __init__(self, connection_url, database_name):
        self.mongo_client = MongoClient(connection_url)
        self.database = self.mongo_client[database_name]

        self.students = self.database["students"]
        self.attendance = self.database["attendance"]

    def add_student(self, name, roll_no, email, course):

        student = {
            "name": name,
            "roll_no": roll_no,
            "email": email,
            "course": course
        }

        existing_student = self.students.find_one({"roll_no": roll_no})

        if existing_student:
            return "Student already exists"

        result = self.students.insert_one(student)
        return result

    def add_attendance(self, roll_no, status):
        student = self.students.find_one({"roll_no": roll_no})

        if not student:
            return "Student not found"

        attendance = {
            "roll_no": roll_no,
            "date": datetime.now(),
            "status": status
        }

        result = self.attendance.insert_one(attendance)
        return result

    def get_all_attendance(self):

        records = list(self.attendance.find())
        return records

    def delete_student(self, roll_no):
        student = self.students.find_one({"roll_no": roll_no})

        if not student:
            print( "Student not found")
            return "Student not found"

        result = self.students.delete_one({"roll_no": roll_no})
        return result
    
    
connection_url ="URL"

manager = AttendanceManager(
    connection_url,
    "college_attendance"
)

manager.add_student(
    "Kuldeep",
    "PY26B012",
    "kdchoudhary5232@gmail.com",
    "Python"
)

manager.add_attendance(
    "PY26B012",
    "Present"
)

records = manager.get_all_attendance()
print(records)

manager.delete_student("PY26B012")
