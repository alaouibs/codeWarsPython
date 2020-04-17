#https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python

def dig_pow(i):
    numberList = str(i)
    power = 1
    sum = 0
    for number in numberList:
        sum = sum + pow(int(number), power)
        power = power + 1
    return sum == i

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    result = []
    for i in range(a, b+1):
        if dig_pow(i):
            result.append(i)
    return result

print(sum_dig_pow(1, 100))