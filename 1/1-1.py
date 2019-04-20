'''
Implement an algorithm to determine if a string has all unique characters.
'''

# Memory: O(1)
# CPU:    O(n*log(n))
def main():
    def is_unique_1(s):
        for i in range(0,len(s)):
            for j in range(i + 1,len(s)):
                if s[i] == s[j]:
                    return False

        return True

    
    # Memory: O(n)
    # CPU:    O(n)
    def is_unique_2(s):
        d = dict()
        for c in s:
            if c in d:
                return False
            else:
                d[c] = True

        return True
    
    
    # Memory: O(1)
    # CPU:    O(n)
    def is_unique(s):
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
