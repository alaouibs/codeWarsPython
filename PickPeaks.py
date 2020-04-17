def pick_peaks(arr):
    delta = 0
    pos = 0
    peak = 0
    output = {"pos": [], "peaks": []}
    for i in range(1, len(arr)):
        delta = arr[i] - arr[i-1]
        print((i, arr[i], delta, pos, peak))
        if delta > 0:
            pos = i
            peak = arr[i]
        if delta < 0 and pos > 0:
            print(i)
            output['pos'].append(pos)
            output['peaks'].append(peak)
            pos = 0
    print(output)
    return output


print(pick_peaks([2,1,3,1,2,2,2,2,1]))