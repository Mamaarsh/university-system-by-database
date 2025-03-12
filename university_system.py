from controlers.database import DataBase
from controlers.show_and_search import show_and_search
from controlers.delete import deletestudent
from controlers.count_and_avguni import count_and_avguni
from controlers.inputs import uni_inputs

userDB = DataBase()
usersershow = show_and_search()
userdel = deletestudent()
usercoavg = count_and_avguni()

print("\nHello and welcome to university system")
while True:
    print("----------------\nPlease choose your option:")
    print("1. Insert student")
    print("2. Show all students")
    print("3. Search students")
    print("4. Delete student")
    print("5. Students count")
    print("6. Average of university")
    print("7. Exit\n----------------\n")
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    print('\n')
    match choice:
        case 1:
            student_data = uni_inputs()
            studentid = input("Please enter student ID: ")
            studentname = input("Please enter student name: ")
            studentlastname = input("Please enter student last name: ")
            while True:
                studentcourses = input("Please enter student's courses (separate by space): ").split()
                try:
                    studentgrades = list(map(int, input("Please enter student grades (separate by space): ").split()))
                except ValueError:
                    print("Invalid input! Please enter numeric grades.\n")
                    continue
                if len(studentcourses) == len(studentgrades):
                    if all(0 <= g <= 20 for g in studentgrades):
                        student_data.insert(studentid, studentname, studentlastname, studentgrades, studentcourses)
                        break
                    else:
                        print("Invalid grade! Enter values between 0-20.\n")
                else:
                    print("Mismatch between number of courses and grades. Please try again.\n")
        case 2:
            usersershow.showallstudents()
        case 3:
            usersershow.searchstudents()
        case 4:
            delstudent = input("Please enter student ID to delete: ")
            userdel.deletestudent(delstudent)
        case 5:
            usercoavg.countofstudents()
        case 6:
            print("Choose your option:")
            print("1. Show Academic average of the university")
            print("2. Show students with GPA higher than university average\n")
            try:
                choose = int(input("Your option: "))
                usercoavg.averageofuniversity(choose)
            except ValueError:
                print("Invalid input! Please enter 1 or 2.")
        case 7:
            userDB.reset_cursor()
            print("BYE!")
            exit(0)
        case _:
            print("Invalid choice! Please enter a number between 1-7.\n")