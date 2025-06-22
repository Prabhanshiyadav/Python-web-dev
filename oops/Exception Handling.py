'''
try
except
'''

num1 = int(input())
num2 = int(input())
nums = [1,2,3]
ans = 0
try:
    ans = num1 // num2
    element = nums[1]
except ZeroDivisorError:
    print("Don't give 0 in num2")
except IndexError:
    print('Watch the index')
else:
    print(f'Quo : {ans}')
    print(f'Element : {element}')
finally:

    print('Done')