import collections


def get_cyclic_path(cycles, tmp, key):
    cycle = ""
    if key == "none":
        for key in tmp.keys():
            if tmp[key]:
                cycle = key
                break


        key = cycle
    else:
        cycle = key

    while tmp[key]:
        cycle += "->"
        key = tmp[key].pop(0)
        cycle += key
    if cycles != "":
        cycle1 = cycle
        cycle2 = cycles
        temp = cycle2.split("->")
        temp.pop()
        temp2 = cycle1.split("->")
        location = temp2.index(temp[0])
        temp2[location] = "&"
        blah = "->".join(temp2)
        location = blah.find("&")
        cycles = cycle1[:location] + "->".join(temp) + "->" + cycle1[location:]
    else:
        cycles = cycle
    return (cycles, tmp)

def main(cycles, tmp):
    temp = cycles.split("->")
    for node in temp:
        if tmp[node] != []:
            return node
    return "completed"



ls = open('data.txt').readlines():
res = {}
for one in ls:
    start = one.split(' ')[0]
    end = one.split(' ')[-1]
    if one.find(','):
        tmp[start] = end.split(',')
    else:
        tmp[start] = [end]


while nextone != "completed":
    temp = get_cyclic_path(cycles, tmp, nextone)
    cycles = temp[0]
    tmp = temp[1]
    nextone = main(cycles, tmp)
print(cycles)