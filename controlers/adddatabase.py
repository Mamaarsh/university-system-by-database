from database import DataBase

class addDatabase:
    def __init__(self, uni_input_instance):
        self.uni_input = uni_input_instance
        self.db = DataBase()
    def calculategpa(self):
        if self.uni_input.studentgrades:
            total_score = sum(self.uni_input.studentgrades)
            self.uni_input.studentgpa = total_score / len(self.uni_input.studentgrades)
            print("\nGPA is", self.uni_input.studentgpa)
        else:
            self.uni_input.studentgpa = 0
            print("\nNo grades available to calculate GPA.")
    def adddatabase(self):
        self.calculategpa()
        db_query = 'INSERT INTO students (ids, sfname, slname, gpa) VALUES (%s, %s, %s, %s)'
        values = (self.uni_input.studentid, self.uni_input.studentname, self.uni_input.studentlastname, self.uni_input.studentgpa)
        self.db.cur.execute(db_query, values)
        for course, grade in zip(self.uni_input.studentcourses, self.uni_input.studentgrades):
            course_query = 'INSERT INTO course (ids, coname, score) VALUES (%s, %s, %s)'
            course_values = (self.uni_input.studentid, course, grade)
            self.db.cur.execute(course_query, course_values)
        self.db.conn.commit()
        print("Added successfully")