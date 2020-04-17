import string
def rot13(message):
    result = ""
    print(message)
    alphabetMin = list(string.ascii_lowercase)
    alphabetMaj = list(string.ascii_uppercase)
    print(alphabetMaj)
    for i in range(0, len(message)):
        if message[i] in alphabetMaj:
            result = result + alphabetMaj[(alphabetMaj.index(message[i]) + 13) % len(alphabetMaj)]
        elif message[i] in alphabetMin:
            result = result + alphabetMin[(alphabetMin.index(message[i]) + 13) % len(alphabetMin)]
        else:
            result = result + message[i]
    return result

print(rot13("test"))