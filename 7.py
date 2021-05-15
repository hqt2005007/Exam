lst = [1, 1, 2, 3, 3] 
outlist = []
for x in range(0,len(lst)):
    if lst.count(x) >= 1:
        outlist.append(x)
print(outlist)
