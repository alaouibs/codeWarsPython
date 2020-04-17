def longest(s1, s2):
    s3 = s1 + s2
    setS = set(s3)
    return ''.join(sorted(list(setS)))
    # your code

longest("aretheyhere", "yestheyarehere")