strs = ["flower","flow","flight"]
shortest = min(strs,key=len)
#for i, ch in enumerate(shortest):
#   print (i,ch)
for i in range(len(strs[1])):
    for other in strs:
        print (other[i])
        
