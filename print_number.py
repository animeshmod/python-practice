n = range(0,7)

for n in n:
    if n%2 == 0 and n in range(6,20):
        print('Weird1')
    elif n%2 == 0 and n in range(2,5):
        print("Not Weird1")
    elif n%2 == 0 and n > 20:
        print("Not Weird2")
    elif n%2 != 0:
        print("Weird2")

