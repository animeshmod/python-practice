x = input()
y = int(input())

m = int(len(x)/y)

k = 0
j = y

for i in range(m+1):
    
    a = x[k:j]
    b = list(set(a))
    c = ''.join(map(str,b))
    k += y
    j += y



    
    print(k,j)
    print(a)
    print(b)
    print(c)


