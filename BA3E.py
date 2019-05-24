data = open('data.txt').readlines()
# print(data)
tmp = {}
num = len(data[1])
for i in data:
    suffix = i[:-1]
    prefix = i[1:]
    if i in tmp:
        tmp[i].append(prefix)
    else:
        tmp[i] = [prefix]
for k in sorted(tmp.keys()):
    res = k + ' -> '
    res += ','.join(sorted(tmp[k]))
    print(res)