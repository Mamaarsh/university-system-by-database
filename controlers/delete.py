from database import DataBase

class deletestudent(DataBase):
    def deletestudent(self, studentid):
        self.cur.execute("SELECT COUNT(*) FROM students WHERE ids = %s", (studentid,))
        student_exists = self.cur.fetchone()[0]
        if student_exists == 0:
            print("Student not found")
            return
        try:
            self.cur.execute("DELETE FROM course WHERE ids = %s", (studentid,))
            self.cur.execute("DELETE FROM students WHERE ids = %s", (studentid,))
            if hasattr(self, "studentid") and studentid in self.studentid:
                index = self.studentid.index(studentid)
                self.studentid.pop(index)
                self.studentname.pop(index)
                self.studentlastname.pop(index)
            print("Deleted successfully")
            self.reset_cursor()
        except Exception as e:
            print("Error deleting student:", e)