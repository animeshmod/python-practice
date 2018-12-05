from itertools import permutations
x = input()
y = []
k = []

for a in x:
    y.append(a)
print(*y)

for n in range(len(y)):
    j=0
    for j in range(len(y)):
        c = y[n] + y[j]
        k.append(c)
        j += 1
    n += 1

print(*k)
a = sorted(list(permutations(y,2)))
for k in a:
    print ("".join(k))

