marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

print(marksheet)

second_highest = sorted(list(set([marks for name, marks in marksheet])),reverse=True)[1]
print(second_highest)
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))