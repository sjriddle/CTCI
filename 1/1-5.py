def is_one_away(s1, s2):
    if len(s1) == len(s2):
        return replace(s1, s2)
    else:
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        return insert(s1, s2)

def insert(s1, s2):
    i1 = i2 = 0
    one_off = False
    while i1 < len(s1):
        if s1[i1] == s2[i2]:
            i1 += 1
            i2 += 1
        else:
            if one_off:
                return False
            one_off = True
            i2 += 1

    return True


def replace(s1, s2):
    one_off = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if one_off:
                return False
            one_off = True
        i += 1

    return True

tests = [
    ("pale", "ple", True),
    ("pales", "pale", True),
    ("pale", "pales", True),
    ("pale", "bale", True),
    ("pale", "bake", False),
]
for t in tests:
    result = is_one_away(t[0], t[1])
    expected_result = t[2]
    print('"%s" - "%s": %s' % (t[0], t[1], 'Pass' if result == expected_result else 'Fail'))

print()
