# student.py
from college import College  # Adjust if it's inside a folder: from oops.college import College

class Student(College):
    def __init__(self, rno, sname, sdept, sph, m1, m2, m3, cname, caddr, noofdept):
        super().__init__(cname, caddr, noofdept)
        self.rollno = rno
        self.sname = sname
        self.sdept = sdept
        self.contact = sph
        self.mark1 = m1
        self.mark2 = m2
        self.mark3 = m3

    def calc_total(self):
        return self.mark1 + self.mark2 + self.mark3

    def calc_average(self):
        return self.calc_total() / 3
