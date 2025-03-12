from database import DataBase

class show_and_search(DataBase):
    def showallstudents(self):
        self.reset_cursor()
        self.cur.execute("SELECT * FROM students ORDER BY slname")
        datas = self.cur.fetchall()
        if datas:
            for data in datas:
                print(data)
        else:
            print("No data exists!")
    def searchstudents(self):
        inputsearch = input("Please enter student ID: ")
        self.reset_cursor()
        query = '''SELECT students.ids, students.sfname, students.slname, students.gpa, 
                          course.coname, course.score 
                   FROM students 
                   LEFT JOIN course ON students.ids = course.ids 
                   WHERE students.ids = %s'''
        self.cur.execute(query, (inputsearch,))
        datas = self.cur.fetchall()
        if datas:
            print(f"\nStudent ID: {datas[0][0]}")
            print(f"Name: {datas[0][1]} {datas[0][2]}")
            print(f"GPA: {datas[0][3]}\n")
            print("Courses:")
            for row in datas:
                print(f"- {row[4]} (Score: {row[5]})")
        else:
            print("\nNo data found for the given student ID.")