a = "Tactb Cab"
b = a.lower().replace(" ","")
len_b = len(b)
c = {}

for char in b:
    if char in c:
        c[char] += 1
    else:
        c[char] = 1

if len_b%2 == 0:
    single_num_count = 0
    for val in c.values():
        if val%2 != 0:
            single_num_count += 1
    if single_num_count != 0:
        print("string is not permutation")
    else:
        print("string is permutation")

if len_b%2 != 0:
    single_num_count = 0
    for val in c.values():
        if val%2 != 0:
            single_num_count += 1
    if single_num_count == 1:
        print ("string is permutation")
    else:
        print("string is not permutation")

