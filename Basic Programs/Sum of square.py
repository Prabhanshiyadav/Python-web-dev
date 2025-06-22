num = int(input("Enter num of terms: "))
summ = 0
for n in range(1, num+1, 2):
    summ += n ** 2
print(f'sum of Sq: {summ}')