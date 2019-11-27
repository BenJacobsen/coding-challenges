# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
dict = {}
inp = sys.stdin.readlines()[1:]
for i in range(len(inp)):
    if i < len(inp) - 1:
        inp[i] = inp[i][0:-1]
    dict[inp[i]] = dict[inp[i]] + 1 if inp[i] in list(dict.keys()) else 1
print(str(len(dict.values())) + '\n' + ' '.join(str(x) for x in sorted(dict.values(), reverse=True)) + '\n')
