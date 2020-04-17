
def validBraces(string):
    pairBraces = {'(':')', '{':'}', '[':']', ')':'(', '}':'{', ']':'['}
    parenthesis = []
    for c in string:
        if c == '(' or c == '{' or c == '[':
            parenthesis.append(c)
        else:
            if len(parenthesis) == 0:
                return False
            elif pairBraces[c] == parenthesis[-1]:
                parenthesis.pop()
            else:
                return False

    return len(parenthesis) == 0


print(validBraces("[(])"))