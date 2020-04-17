def increment_string(strng):
    number = 0
    output = ""
    numberDigit = 0
    findNotDigit = False
    k = 0
    for i in range(len(strng) - 1, -1, -1):
        if strng[i].isdigit() and not findNotDigit:
            numberDigit = numberDigit + 1
            number = number + int(strng[i])*(10**k)
            k = k + 1
        else:
            findNotDigit = True
            output = strng[i] + output
    number = number + 1
    number = str(number)
    for i in range(len(number), numberDigit):
        number = "0" + number
    return output + number

print(increment_string("foobar099"))
print(increment_string("pub~:49409028W|aJTV~.52337]fxBG^k69|A!Ezhyx84754486=lT3O)118yY]-\"43376291eE\'Jb`2778728792500"))