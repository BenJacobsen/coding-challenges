import sys, re
max_chars = {}
#take in strings and print max occurances of characters per line
for line in open(sys.argv[1]).readlines():
    chars = {}
    for char in [x for x in line if x >= 'a' and x <= 'z']:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    for key,value in chars.items():
        if (not key in max_chars) or max_chars[key] < chars[key]:
            max_chars[key] = chars[key]
for key,value in max_chars.items():
    print("Character:{}   Max occurances: {}".format(key, value))