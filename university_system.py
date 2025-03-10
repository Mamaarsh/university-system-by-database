import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', password='M@m@rsh!a1384_', database='university')
cur = conn.cursor()

class university:
    def __init__(self):
        cur.execute('select ids from students')
        iddata = cur.fetchall()
        listid = [item for item in iddata]
        self.studentid = listid
        cur.execute('select sfname from students')
        fndata = cur.fetchall()
        listfname = [item for item in fndata]
        self.studentname = listfname
        cur.execute('select slname from students')
        snamedata = cur.fetchall()
        listlname = [item for item in snamedata]
        self.studentlastname = listlname
        self.studentgrades = []
        self.studentgpa = 0
        self.studentcourses = []



    def insert(self, studentid, studentname, studentlastname, studentgrades, studentcurses):
        self.studentid = studentid
        self.studentname = studentname
        self.studentlastname = studentlastname
        n = len(studentgrades)
        for i in range(n):
            self.studentgrades.append(studentgrades[i])
            self.studentcourses.append(studentcurses[i])

        print("Want add into data base?(y/n)")
        if input().lower() == 'y':
            university.adddatabase(self)
        else:
            print("\nOk")

    def calculategpa(self):
        for i in self.studentgrades:
            self.studentgpa += int(i)
        self.studentgpa /= len(self.studentgrades)
        print("\nGPU is ", self.studentgpa)

    def adddatabase(self):
        print("Are you calculate gpu?(y/n)")
        if input().lower() == 'n':
            university.calculategpa(self)
        db = 'insert into students(ids, sfname, slname, gpa) values(%s,%s,%s,%s)'
        value = (self.studentid, self.studentname, self.studentlastname, self.studentgpa)
        cur.execute(db, value)
        for course, grade in zip(self.studentcourses, self.studentgrades):
            course_query = 'insert into course(ids, coname, score) values(%s,%s,%s)'
            course_value = (self.studentid, course, grade)
            cur.execute(course_query, course_value)
        conn.commit()
        print("Added successfully")

    def showallstudents(self):
        cur.execute("select * from students order by slname")
        datas = cur.fetchall()
        if datas:
            for data in datas:
                print(data)
        else:
            print("No data exist!")

    def searchstudents(self):
        print("Please enter student id: ")
        inputsearch = input()
        query = 'select students.ids, students.sfname, students.slname, students.gpa, course.coname, course.score \
                 from students join course on students.ids = course.id where students.ids'
        cur.execute(query, (inputsearch,))
        datas = cur.fetchall()
        if datas:
            print(f"\nStudent ID: {datas[0][0]}")
            print(f"Name: {datas[0][1]} {datas[0][2]}")
            print(f"GPA: {datas[0][3]}")
            print("\nCourses:")
            for row in datas:
                print(f"- {row[4]} (Score: {row[5]})")
        else:
            print("\nNo data exists!")

    def deletestudent(self, studentid):
        deleted = False
        orgstid = '('+studentid+',)'
        for i in self.studentid:
            if str(i) == orgstid:
                cur.execute("delete from students where ids = %s",(studentid))
                conn.commit()
                self.studentid.remove(studentid)
                print("Deleted successfully")
                deleted = True
                break
        if not deleted:
            print("Student not found")

    def countofstudents(self):
        cur.execute("select count(ids) from students")
        data = cur.fetchall()
        print("Number of students: ",data[0][0])

    def averageofuniversity(self, choose):
        if choose == 1:
            cur.execute("select avg(gpa) from students")
            data = cur.fetchall()
            if data[0][0] is not None:
                print("Academic average of the university is: ", data[0][0])
            else:
                print("\nNo data exist!")
        elif choose == 2:
            cur.execute("select * from students where gpa > (select avg(gpa) from students)")
            data = cur.fetchall()
            for datas in data:
                print(datas)
            cur.execute("select count(ids) from students where gpa > (select avg(gpa) from students order by gpa)")
            cdata = cur.fetchall()
            print("\nNumber of students: ",cdata[0][0])
        else:
            print("Invalid option")



unisys = university()
print("\nHello and welcome to university system")
while True:
    print("----------------\nPlease choose your option:")
    print("1.Insert student")
    print("2.Calculate GPU")
    print("3.Add database")
    print("4.Show all students")
    print("5.Search students")
    print("6.Delete student")
    print("7.Students count")
    print("8.Average of university")
    print("9.Exit\n----------------\n")
    choice = int(input("Your choice:"))
    print('\n')
    match choice:
        case 1:
            flag = False
            studentid = input("Please enter student id: ")
            studentname = input("Please enter student name: ")
            studentlastname = input("Please enter student last name: ")
            while not flag:
                flag = True
                studentcourses = []
                studentgrades = []
                sc = input("Please enter students courses: ").split()
                sg = list(map(int, input("Please enter student grades: ").split()))
                if len(sc) == len(sg):
                    for i in sc:
                        studentcourses.append(i)
                    for i in sg:
                        if i >= 0 and i <= 20:
                            studentgrades.append(i)
                        else:
                            print("Invalid input!\nPlease try again\n")
                            flag = False
                            break
                    if flag:
                        unisys.insert(studentid, studentname, studentlastname, studentgrades, studentcourses)
                else:
                    print("Grades over then courses please try again\n")
        case 2:
            unisys.calculategpa()
        case 3:
            unisys.adddatabase()
        case 4:
            unisys.showallstudents()
        case 5:
            unisys.searchstudents()
        case 6:
            delstudent = input("Please enter student id for delete: ")
            unisys.deletestudent(delstudent)
        case 7:
            unisys.countofstudents()
        case 8:
            print("Choose your option: ")
            print("1.Show Academic average of the university")
            print("2.Show the GPA of students who are higher than the academic GPA of the university\n")
            choose = int(input("Your option: "))
            unisys.averageofuniversity(choose)
        case 9:
            cur.close()
            conn.close()
            print("BYE!")
            exit(0)