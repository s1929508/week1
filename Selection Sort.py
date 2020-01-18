
def  SelectSort(ls):
    n=len(ls)
    if n<=1:
        return ls
    for i in range(0,n-1):
        minIndex=i
        for j in range(i+1,n):  #Compare and record the index, but do not exchange
            if ls[j]<ls[minIndex]:
                minIndex=j
        if minIndex!=i:                     #Exchange the number by index
            (ls[minIndex],ls[i])=(ls[i],ls[minIndex])
    return ls
