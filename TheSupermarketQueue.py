#https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python

def queue_time(customers, n):
    currentTime = 0
    cashierIlls = {}

    for i in range(1, n+1):
        cashierIlls[i] = 0
    for i in range(0, len(customers)):
        cashierAvailable = min(cashierIlls, key = cashierIlls.get)
        cashierIlls[cashierAvailable] = cashierIlls[cashierAvailable] + customers[i] 
    return cashierIlls[max(cashierIlls, key=cashierIlls.get)]


print(queue_time([2,2,3,3,4,4], 2))
print(queue_time([2], 5))