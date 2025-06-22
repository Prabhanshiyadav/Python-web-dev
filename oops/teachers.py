from oops.college import College
class Teachers(College):
    def __init__(self, name, caddr, noofdept, eid, tname, tdept, tsal):
        super().__init__(cname, caddr, noofdept)
        self.empid = eid
        self.tname = tname
        self.tdept = tdept
        self.sal = tsal
    def display_teacher_info(self):
        print(f'Emp id : {self.empid}')
