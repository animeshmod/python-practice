x = int(input())
i = map(int,input().split())

integer_list = tuple(i)

k = hash(integer_list)

print (integer_list)
print(k)