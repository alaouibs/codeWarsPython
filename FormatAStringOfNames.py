def namelist(names):
    if len(names) == 1:
        return names[0]['name']
    result = ""
    for i in range(0, len(names) - 1):
        result = result + names[i]['name'] + ", "
    result = result[:-2]
    return result + " & " + names[len(names) - 1]['name']

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])