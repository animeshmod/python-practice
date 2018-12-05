x = int(input("Enter side 1"))
y = int(input("Enter side 2"))
z = int(input("Enter side 3"))
n = int(input("Enter side n"))

print [[x, y, z] for x in range(x+1) for y in range(y+1) for z in range(z+1) if ((x+y+z) != n)]
