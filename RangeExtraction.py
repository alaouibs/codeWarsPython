import copy
def solution(args):
    start = 0
    end = 1
    rangeExtraction = []
    current = args[start]
    while start < len(args) - 1:
        print((args[start], args[end], current))
        if args[end] == current + 1:
            print("yes")
            current = args[end]
            end = min(end + 1, len(args) - 1)
        else:
            if len(args[start:end]) == 1:
                rangeExtraction.append([args[start]])
            elif len(args[start:end]) == 2:
                rangeExtraction.append([args[start]])
                rangeExtraction.append([args[start + 1]])
            else:
                rangeExtraction.append([args[start], args[end - 1]])
            start = end
            end = min(end + 1, len(args) - 1)
            current = args[start]
    if args[-1] == rangeExtraction[-1][-1] + 1:
        rangeExtraction[-1].append(args[-1]) 
    else:
        rangeExtraction.append([args[-1]])
    print(rangeExtraction)
    for i in range(0, len(rangeExtraction)):
        if len(rangeExtraction[i]) == 1:
            rangeExtraction[i] = str(rangeExtraction[i][0])
        else:
            rangeExtraction[i] = str(rangeExtraction[i][0]) + "-" + str(rangeExtraction[i][-1])
    return ','.join(rangeExtraction)


print(solution([-6, -3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))