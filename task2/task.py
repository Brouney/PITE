# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
# Try to expand your implementation as best as you can.
# Think of as many features as you can, and try implementing them.
# Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
# Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
# The goal of this task is for you to SHOW YOUR BEST python programming skills.
# Impress everyone with your skills, show off with your code.
#
# Your program must be runnable with command "python task.py".
# Show some usecases of your library in the code (print some things)
#
# When you are done upload this code to your github repository.
#
# Delete these comments before commit!
# Good luck.


import json
import statistics
import numpy as np


def add_classes(register, clas):
    tmpclas = {
        "number": clas
    }
    register["allclasses"].append(tmpclas)


def make_register() -> dict:
    tmpregister = {
        "allstudents": [],
        "allclasses": [],
        "allgrades": [],
        "allattendance": [],
        "allsubjects": []
    }
    return tmpregister


def add_student(register, name, surname, clas):
    tmpstud = {
        "id": len(register["allstudents"]),
        "name": name,
        "surname": surname,
        "clas": clas
    }
    register["allstudents"].append(tmpstud)


def add_mark(register, idd, subject, mark1):
    tmpmark = {
        "studid": idd,
        "subject": subject,
        "mark": mark1
    }
    register["allgrades"].append(tmpmark)


def attendance(register, attend, idd, subject):
    tmpattendance = {
        "studid": idd,
        "subject": subject,
        "attend": attend
    }
    register["allattendance"].append(tmpattendance)


def add_subject(register, subj):
    tmpsubj = {
        "name": subj
    }
    register["allsubjects"].append(tmpsubj)


def get_stud_id(register, name, surname, clas):
    for tmp in register["allstudents"]:
        if tmp["name"] == name and tmp["surname"] == surname and tmp["clas"] == clas:
            return tmp["id"]


def mean_across_subj(register, subject):
    table = []
    for tmp in register["allgrades"]:
        if tmp["subject"] == subject:
            table.append(tmp["mark"])
    return statistics.mean(table)


def mean_all_courses_for_a_student(register, studid):
    reg2 = register["allgrades"]
    table2 = []
    table = list( filter( lambda x : x["studid"] == studid, reg2))

    for tmp in table:
        table2.append(tmp["mark"])
    
    return statistics.mean(table2)


def mean_across_all_courses(register):
    table = []
    for tmp in register["allgrades"]:
        table.append(tmp["mark"])
    return statistics.mean(table)

def save_to_json(register):
    file = open("file.json", "w")
    json.dump(register, file, indent=4)
    file.close()

def read_from_json()->dict:
    file = open("file.json", "r")
    register = json.load(file)
    file.close()
    return register

def count_attendance_to_student(register,idstud):
    reg2 = register["allattendance"]
    table2 = []
    att = 0
    table = list( filter( lambda x : x["studid"] == idstud, reg2))

    for tmp in table:
        table2.append(tmp["attend"])
        att += tmp["attend"]
    
    return (att/len(table2))

def mark_and_attendance_generator(register,idstud):
    for i in range(3):
        for j in range(8):
            add_mark(register, idstud, register["allsubjects"][i]["name"], np.random.randint(1,7))
    
    for i in range(3):
        for j in range(8):
            attendance(register, np.random.randint(0,2), idstud, register["allsubjects"][i]["name"])

def main_program_1(register):
    add_student(register, "Peter", "Parker", "1")
    add_student(register, "Wladimir", "Poarker", "2")
    add_student(register, "Spike", "Bike", "1")

    
    idstud = get_stud_id(register, "Wladimir", "Poarker", "2")
    mark_and_attendance_generator(register,idstud)
   
    idstud = get_stud_id(register, "Peter", "Parker", "1")
    mark_and_attendance_generator(register,idstud)

    idstud = get_stud_id(register, "Spike", "Bike", "1")
    mark_and_attendance_generator(register,idstud)
    

    mean = mean_across_subj(register, "Physics")
    print("mean for subject - all students in courses: {} is {}".format("Physics", str(mean)))

    mean = mean_all_courses_for_a_student(register, idstud)
    print("mean for Spike Bike on all courses: {}".format(str(mean)))

    mean = mean_across_all_courses(register)
    print("mean for all courses and all students: {}".format(str(mean)))

    attendancee = count_attendance_to_student(register,idstud)
    print("Attendance in % of Spike Bike on all courses: {}".format(str(attendancee)))

    save_to_json(register)
    print("zapisano do pliku.")

    register = read_from_json()
    print("zapisano z pliku.")


def main_program_2(register):
    while True:
        option = input("if you want to add student press 1, if you want to add mark press 2, if you want to know mean grades press 3,\n if you want to save to file press 4, if you want to quit press 0: ")
        if option == '1':
            main_program_2_option_1(register)

        if option == '2':
            main_program_2_option_2(register)

        if option == '3':
            main_program_2_option_3(register)

        if option == '4':
            save_to_json(register)

        if option == '0':
            break


def main_program_2_option_1(register):
    name = input("Write name: ")
    surname = input("Write surname: ")
    clas = int(input("Write class 1-3: "))
    add_student(register, name, surname, clas)


def main_program_2_option_2(register):
    name = input("Write name for recognise: ")
    surname = input("Write surname: ")
    clas = int(input("Write class 1-3: "))
    subject = input("Write subject: ")
    mark = int(input("Write mark 1-6: "))
    idstud = get_stud_id(register, name, surname, clas)
    add_mark(register, idstud, subject, mark)


def main_program_2_option_3(register):
    option2 = input(
        "Mean across: students in subject press 1, courses in school(all students) press 2, mean of all courses for a student press 3: ")
    if option2 == '1':
        subject = input("Write subject: ")
        mean = mean_across_subj(register, subject)
        print("\nmean for subject: {} is {}\n".format(subject, str(mean)))
    if option2 == '2':
        mean = mean_across_all_courses(register)
        print("\nmean for all courses and all students: {}\n".format(str(mean)))
    if option2 == '3':
        name = input("Write name for recognise: ")
        surname = input("Write surname: ")
        clas = int(input("Write class 1-3: "))
        idstud = get_stud_id(register, name, surname, clas)
        mean = mean_all_courses_for_a_student(register, idstud)
        print("\nmean for Spike Bike on all courses: {}\n".format(str(mean)))


if __name__ == "__main__":
    register = make_register()

    add_classes(register, 1)
    add_classes(register, 2)
    add_classes(register, 3)

    add_subject(register, "Math")
    add_subject(register, "English")
    add_subject(register, "Physics")

    program = input(
        "if you want to make auto program press 1, if you want to manually add students etc press 2: ")

    if program == '1':
        main_program_1(register)

    if program == '2':
        main_program_2(register)
