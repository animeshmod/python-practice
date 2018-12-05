def PalindromicSubstring(s):
    len_s = len(s)
    max_len = 1
    pal_str = 'a'

    for i in range(len_s):
        for j in range(len_s):
            a = s[i:j+1]
            b = a[::-1]
            c = len(a)

            if a == b and c > max_len:
                max_len = c
                pal_str = a
    return pal_str

def FasterPalindromicSubstring(s):
    len_s = len(s)
    max_len = 1
    start = 0

    high = 0
    low = 0

    for i in range(1,len_s):
        # for even length string
        low = i-1
        high = i

        while low >= 0 and high < len_s and s[low] == s[high]:
            if high - low + 1 >= max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1

        # for odd length string
        low = i-1
        high = i+1

        while low >= 0 and high < len_s and s[low] == s[high]:
            if high - low + 1 >= max_len:
                start = low
                max_len = high - low + 1
            
            low -= 1
            high += 1

    return s[start:start+max_len]


s = 'babad'

long_str = FasterPalindromicSubstring(s)

print (long_str)

