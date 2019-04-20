'''
Implement an algorithm to determine if a string has all unique characters.
'''


def main():
    def is_unique_1(s): # t: O(n*log(n)), m: O(1)
        for i in range(0,len(s)):
            for j in range(i + 1,len(s)):
                if s[i] == s[j]:
                    return False

        return True

    def is_unique_2(s): # t: O(n), O(n)
        d = dict()
        for c in s:
            if c in d:
                return False
            else:
                d[c] = True

        return True

    def is_unique(s): # t: O(n), m: O(1)
        bit_vector = 0
        for c in s:
            i = int(2 ** (ord(c) - 97))
            if i & bit_vector:
                return False
            else:
                bit_vector |= i

        return True

    tests = {
        'abcd': True,
        'aab': False,
        'qwertyuiop[]': True,
        'abcdedk': False,
    }
    for s, expected_result in tests.items():
        result = is_unique(s)
        print('%s: %s' % (s, 'Pass' if result == expected_result else 'Fail'))

    print()

if __name__ == '__main__':
    main()


# n + n-1 + n-2 + n-3 + ... + 2 + 1
# 1 + 2 + ... + n-2 + n-1 + n
