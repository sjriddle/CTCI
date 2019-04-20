def is_perm_palindrome(url):
    pass


tests = [
    ("John Doe  ", "John%20Doe"),
]
for t in tests:
    result = is_perm_palindrome(t[0])
    expected_result = t[1]
    print('"%s" - "%s": %s' % (t[0], result, 'Pass' if result == expected_result else 'Fail'))

print()
