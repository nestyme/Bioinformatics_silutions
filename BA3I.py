import collections   
import itertools

path = []
s = '0'*(8-1)
string_2 = int('1'* 8, 2)

tmp_n = collections.defaultdict(list)
for i in range(0,int('1'* 8, 2)+1):
    a = (bin(i)[2:].zfill(8))
    if not(a=="1"+('0'* 7) or a=='0'*8):
            s = a[0:7]
            e = a[1:8]
            tmp_n[s].append(a[1:8])
            tmp_n[e].append(a[0:7])
path = []
s = '0'*(8-1)
path.append('0'*(8-1))
while(len(tmp_n['0'*(8-1)])>0):
    begins = s[1:len(s)]
    if begins+"1" in  tmp_n[s]:
        path.append(begins+"1")
        tmp_n[s].remove(begins+"1")
        tmp_n[begins+"1"].remove(s)
        s = begins+"1"
    else:
        path.append(begins+"0")
        tmp_n[s].remove(begins+"0")
        tmp_n[begins+"0"].remove(s)
        s = begins+"0"      

result ='0'
with open('result.txt', 'w') as file:
    for i,j in enumerate(path):
        result+=j[0]
    file.write(result)

