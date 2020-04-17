def sqInRect(lng, wdth):
    if lng == wdth:
        return None
    result = []

    while lng != wdth:
        if lng > wdth:
            result.append(wdth)
        lng = lng - wdth
        if lng < wdth:
            tmp = lng
            lng = wdth
            wdth = tmp
    result.append(1)
    return result

print(sqInRect(5, 3))