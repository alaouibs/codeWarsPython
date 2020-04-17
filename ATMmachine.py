def validate_pin(pin):
    if not (len(pin) == 4 or len(pin) == 6):
        return False
    pinDigits = set(pin)
    for a in pinDigits:
        if not a.isdigit():
            return False
    return True

print(validate_pin("a234"))