from database import DataBase

class count_and_avguni(DataBase):
    def __init__(self):
        super().__init__()
    def countofstudents(self):
        self.cur.execute("SELECT COUNT(*) FROM students")
        count = self.cur.fetchone()[0]
        print(f"\nTotal students: {count}")
    def averageofuniversity(self, option):
        if option == 1:
            self.cur.execute("SELECT AVG(gpa) FROM students")
            avg_gpa = self.cur.fetchone()[0]
            if avg_gpa != None:
                print(f"\nUniversity average GPA: {avg_gpa}")
            else:
                print(f"\nNo data for university average GPA")
        elif option == 2:
            self.cur.execute("select * from students where gpa > (select avg(gpa) from students)")
            data = self.cur.fetchall()
            for datas in data:
                print(datas)
            self.cur.execute("select count(ids) from students where gpa > (select avg(gpa) from students order by gpa)")
            cdata = self.cur.fetchall()
            print("\nNumber of students: ", cdata[0][0])
        else:
            print("\nInvalid option")