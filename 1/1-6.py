def compress(s):
    if s == '':
        return s

    res = []
    cc = None
    cnt = 0

    for i in range(len(s)):
        if cc == s[i]:
            cnt += 1
        else:
            if cc is not None:
                res.append(cc)
            if cnt > 1:
                res.append(str(cnt))
            cc = s[i]
            cnt = 1
    else:
        res.append(cc)
        if cnt > 1:
            res.append(str(cnt))

    return ''.join(res)


tests = [
    ("abcd", "abcd"),
    ("aabcd", "a2bcd"),
    ("aaabbcd", "a3b2cd"),
    ("", ""),
    ("aaaa", "a4"),
]
for t in tests:
    result = compress(t[0])
    expected_result = t[1]
    print('"%s": "%s" - "%s": %s' % (t[0], expected_result, result, 'Pass' if result == expected_result else 'Fail'))

print()
