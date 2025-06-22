cnm = input('College Name ')
cad = input('College addr ')
depts = input('Department  ')
pno = input('Roll no  ')
snm = input('Stud name  ')
sdept = input('Stud name  ')
phno = int(input('Phone no  '))
m1 = int(input('Mark 1 '))
m2 = int(input('Mark 2 '))
m3 = int(input('Mark 3 '))
stud = Student(cname = cnm, caddr = cad, rno = rno, noofdept = depts, sname = snm, sdept = sdept, sph = phno, m1 = m1, m2 = m2, m3 = m3)
stud.display_collegeinfo()
print(f'Stu Rno : {stud.rollno} Name : {stud.sname} Dept : {stud.sdept}'
      f'Average Score : {stud.calc_average()}')

teacher = Teachers(cname = cnm, caddr = cad, noofdept = depts, eid = eid, tname = tnm, tdpet = tdpet, tsal = sal)
teacher.display_teacher_info()

