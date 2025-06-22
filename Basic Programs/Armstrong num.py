user_value = int(input('enter a num: '))
orig = user_value
summ = 0
while user_value > 0:
    rem = user_value % 10
    summ = summ + (rem ** 3)
    user_value = user_value // 10
if summ == orig:
    print('Armstrong no')
else:
    print("Not_Armstrong no")