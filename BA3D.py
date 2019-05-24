import collections

string = open('data.txt', 'r').read()
k = 12
start = 0
res = {}
while start + k <= len(string):
    w = string[start:start+k]
    pre, suf = w[:-1], w[1:]
    if pre not in res:
        res[pre] = (suf,)
    else:
        res[pre] += (suf,)
    start += 1

tmp = collections.OrderedDict(sorted(res.items()))
with open('result.txt', 'w') as file:
    for key in tmp.keys():
        file.write(str(key) + " -> ")
        if len(res[key]) == 1:
            file.write(res[key][0] + "\n")
        else:
            # print(res[key])
            res[key] = sorted(res[key])
            file.write(res[key][0])
            del res[key][0]
            for item in res[key]:
                file.write("," + str(item))

            file.write("\n")