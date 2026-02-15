import sys
data = map(lambda x: x.rstrip(), sys.stdin.readlines())
res = []
N = 1
for i in data:
    if int(i) == N:
        res.append(i)
    N += 1
with open("output.txt", "w") as fout:
    if res:
        fout.write(" ".join(res))
    else:
        fout.write("0")