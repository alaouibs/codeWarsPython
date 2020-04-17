def repet(x):
    xDict = {}
    for i in x:
        if i in xDict:
            xDict[i] = xDict[i] + 1
        else:
            xDict[i] = 0
    return [k for k in xDict if xDict[k] > 0]

def printRepeating(arr, size): 
      
    print("The repeating elements are: ") 
    for i in range(0, size): 
        if arr[abs(arr[i])] >= 0: 
            arr[abs(arr[i])] = -arr[abs(arr[i])] 
        else: 
            print (abs(arr[i]) + " ") 

l = [1, 2, 3, 1, 3, 6, 6]
print(repet(l))

