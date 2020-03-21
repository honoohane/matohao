import os

f = open(os.getcwd() + 'musicinfo.txt')
data = f.readlines()
datafinal = []
for i in data:
    datafinal.append(i)
diyihang = data[0]
disanhang = data[2]
ff = open("input.txt")
fff = open("result.txt", "w")
variables = ff.readlines()
for i in range(int(variables[2])):
    k = int(variables[0]) + i
    s = data[0].replace('rankofsong', str(k))
    datafinal[0] = s
    data[0] = diyihang
    k = int(variables[1]) + i
    s = data[2].replace('startid', str(k))
    datafinal[2] = s
    data[2] = disanhang
    for j in datafinal:
        fff.write(j)
f.close()
ff.close()
fff.close()
