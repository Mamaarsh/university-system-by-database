from database import DataBase
from adddatabase import addDatabase

class uni_inputs(DataBase):
    def __init__(self):
        super().__init__()
    def insert(self, studentid, studentname, studentlastname, studentgrades, studentcourses):
        self.studentid = studentid
        self.studentname = studentname
        self.studentlastname = studentlastname
        self.studentgrades = studentgrades
        self.studentcourses = studentcourses
        print("Want to add into database? (y/n)")
        if input().lower() == 'y':
            adddb = addDatabase(self)
            adddb.adddatabase()
        else:
            print("\nOk")