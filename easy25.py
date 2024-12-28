def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


l = [n for n in range(154771, 164752 + 1)]
primeNumbersList = [2]
numWithMaxDigSum = 0
maxDigSum = 0

for i in range(3, (164752 + 1) // 2):
    flag = True
    for j in primeNumbersList:
        if i % j == 0:
            flag = False
            break
    if flag:
        primeNumbersList.append(i)


for i in l:
    counterOfPrimeDivisors = 0
    for j in primeNumbersList:
        if i % j == 0:
            counterOfPrimeDivisors += 1

    if counterOfPrimeDivisors == 6:
        digSum = sum_of_digits(i)
        if digSum > maxDigSum:
            maxDigSum = digSum
            numWithMaxDigSum = i

print(numWithMaxDigSum)
