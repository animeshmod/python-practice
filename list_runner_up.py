x = int(input("Enter Number of Players:"))
y = [int(y) for y in input().split()]

print (sorted(set(y))[-2])