def urlify(url):
    new_url = []
    i = 0
    while len(new_url) < len(url):
        if url[i] == ' ':
            new_url.extend(['%', '2', '0'])
        else:
            new_url.append(url[i])
        i += 1

    return ''.join(new_url)






tests = [
    ("John Doe  ", "John%20Doe"),
    ("Test", "Test"),
    ("", ""),
    ("   ", "%20"),
    ("a b d    ", "a%20b%20d"),
    ("a  d    ", "a%20%20d"),

]
for t in tests:
    result = urlify(t[0])
    expected_result = t[1]
    print('"%s" - "%s": %s' % (t[0], result, 'Pass' if result == expected_result else 'Fail'))

print()
