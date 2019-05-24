import collections

res = {}

with open('data.txt', 'r') as f:
    data = f.readlines()
for i in range(0, len(data)):
    data[i] = data[i].strip()



for i in range(len(data)):
    for j in range(len(data)):
        if (i != j) and (patterns[i][:-1] == patterns[1:j]):
            res[patterns[i]] = patterns[j]

od = collections.OrderedDict(sorted(res.items()))
with open('result.txt', 'w') as file:
    for key in od.keys():
        file.write(str(key) + " -> " + str(od[key]) + "\n")