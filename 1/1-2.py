from collections import defaultdict


def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    d1 = defaultdict(lambda: 0)
    d2 = defaultdict(lambda: 0)

    for i in range(len(s1)):
        d1[i] += 1
        d2[i] += 1

    return d1 == d2


tests = [
    ("abcde", "abcde", True),
    ("abced", "abcde", True),
    ("abc", "abcc", False),
    ("", "abcc", False),
    ("", "", True),
]
for t in tests:
    result = is_permutation(t[0], t[1])
    expected_result = t[2]
    print('"%s" "%s": %s' % (t[0], t[1], 'Pass' if result == expected_result else 'Fail'))

print()
