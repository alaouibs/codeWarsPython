def valid_parentheses(string):
    parentheise = []
    for c in string:
        if c == '(':
            parentheise.append(c)
        elif c == ')' and len(parentheise) == 0:
            return False
        elif c == ')':
                parentheise.pop()
    return len(parentheise) == 0
    #your code here


print(valid_parentheses("hi(hi)()"))