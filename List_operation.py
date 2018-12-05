x = []
for _ in range(int(input())):
    item = int(input())
    x.append(item)

def insert_object(x, y, z):
    x.insert(y,z)
    return print(x)

def remove_object(x,z):
    x.remove(z)
    return print(x)
def list_sort(x):
    x.sort()
    print(x)
    a = list(reversed(x))
    print(a)
    b = x.pop()
    print(b)

# inser object at position
y = int(input("Insert position:"))
z = int(input("Input object:"))
r = int(input("Number to be removed:"))

insert_object(x,y,z)
remove_object(x,r)
list_sort(x)

