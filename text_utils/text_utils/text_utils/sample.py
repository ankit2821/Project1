L=[2,2,3,4,5,6,6,7,8,8,8,10,3]
for i in range(0,len(L)):
    if L.count(L[i])==2:
        print(L[i])
        L.remove(L[i])
