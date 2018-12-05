y = int(input())
s_record = {}
for _ in range(y):
    name, *line = input().split()
    score = list(map(float, line))
    print(name)
    print(score)
    s_record[name] = score
query = input()

if query in s_record.keys():
    x = s_record[query]
    print (x)
    ave = sum(x)/len(x)
    print(ave)
    
    