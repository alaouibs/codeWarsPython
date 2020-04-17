def binary_array_to_number(arr):
    result = 0
    power = len(arr) - 1
    for i in arr:
        result += i*pow(2,power)
        power = power - 1

    return result
  # your code


print(binary_array_to_number([0,0,0,1]))