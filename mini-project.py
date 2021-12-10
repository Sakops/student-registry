from dataclasses import dataclass
import json
#student registry
@dataclass
class Student:
    name: str = ""
    mark: int = 0
c = """
    a. add student
    s. show students
    e. exit
"""
students = []
while True:
    command = input(c)
    if command == "a":
        student = Student()
        student.name = input("enter name: ")
        student.mark = int(input("enter mark: "))
        students.append(student)
    elif command == "s":
        for student in students:
            print(student.__dict__)
    elif command == "e":
        break


