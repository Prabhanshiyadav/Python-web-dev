# college.py
class College:
    def __init__(self, cname, caddr, noofdepts):
        self.cname = cname
        self.caddr = caddr
        self.no_of_depts = noofdepts

    def display_collegeinfo(self):
        print(f'Name : {self.cname} \t Addr : {self.caddr} \t'
              f'Department count : {self.no_of_depts}')
