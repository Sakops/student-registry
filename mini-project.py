from dataclasses import dataclass
import json
import os

@dataclass
class Student:
    name: str
    mark: int

c = """a. add student
s. show students
d. delete student
e. exit

"""
students = []
if not os.path.exists('./users.json'):
    f = open('users.json','w+')
    f.close()
while True:
    with open("users.json", "r") as f:
        read = f.read()
        if read:
            students_json = json.loads(read)
            students = []
            for s in students_json:
                students.append(Student(**s))
    command = input(c)
    if command == "a":
        student = Student("", 0)
        student.name = input("enter name: ")
        student.mark = int(input("enter mark: "))
        students.append(student)
        with open("users.json", "w") as f:
            students_dict = []
            for s in students:
                students_dict.append(s.__dict__)
            json.dump(students_dict, f)
    elif command == "s":
        for student in students:
            print(student.__dict__)
    elif command == "d": 
        student = Student("", 0)
        student_name = input("name: ")
        name = student_name.index(student_name)
        students.pop(name)
        # student.name = input("Enter student name: ")
        with open("users.json", "w") as f: 
            students_dict = []
            for s in students_dict: 
                students_dict.pop(s.name)
            json.dump(students_dict, f)
    elif command == "e":
        break


