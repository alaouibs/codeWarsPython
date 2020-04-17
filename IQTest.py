import numpy as np


def iq_test(numbers):
    even = set()
    odds = set()
    numbers = numbers.split(" ")
    print(numbers)
    for i in range(0, len(numbers)):
        if int(numbers[i]) % 2 == 0:
            even.add(i+1)
        else:
            odds.add(i+1)
            
    if len(even) == 1:
        return list(even)[0]
    else:
        return list(odds)[0]
    #your code here

np.testing.assert_equal(iq_test("2 4 7 8 10"),3)
np.testing.assert_equal(iq_test("1 2 2"), 1)