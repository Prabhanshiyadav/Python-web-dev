def calc_tot_avg(mark1, mark2, mark3):
    tot = mark1 + mark2 + mark3
    avg = tot / 3
    return tot, avg
sname = input('Enter name: ')
mark1 = int(input('Mark 1: '))
mark2 = int(input('Mark 2: '))
mark3 = int(input('Mark 3: '))

total, average = calc_tot_avg(mark1, mark2, mark3)
print(f'Name : {sname} Total : {total} Avg : {average} ')