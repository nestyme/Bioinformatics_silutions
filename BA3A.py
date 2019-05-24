s = open('data.txt', 'r').read()
strings = []

for c in range(len(s)-49):
    strings.append(s[c:c+50])
    
print('\n'.join(sorted(strings)))