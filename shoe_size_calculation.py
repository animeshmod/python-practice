from collections import Counter
x = input()
z = list(map(int,input().split()))
n_o_c = int(input())
unique_size = list(set(z))
y = {}
profit = 0

for number in unique_size:
    y[number] = z.count(number)
print(y)
print(z)

for customer in range(n_o_c):
    size, price = map(int, input().split())
    if size in y and y[size] > 0:
        print(size)
        profit += price
        y[size] -= 1
print(profit)
    
