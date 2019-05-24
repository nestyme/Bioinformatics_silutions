s = open('data.txt', 'r').read()
strings = s.split('\n')
strings = strings[:-1]
result = ''
for string in strings:
    result += string[0]
result += strings[-1][1:]