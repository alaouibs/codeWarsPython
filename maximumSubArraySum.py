def max_sequence(arr):
    maxSoFar = 0
    maxEnding = 0
    for number in arr:
        maxEnding = maxEnding + number
        if maxEnding < 0:
            maxEnding = 0
        if maxSoFar < maxEnding:
            maxSoFar = maxEnding
    return maxSoFar


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))