def BubbleSort(ls):
    n=len(ls)
    if n<=1:
        return ls
    for i in range (0,n):
        for j in range(0,n-i-1):
            if ls[j]>ls[j+1]:
                (ls[j],ls[j+1])=(ls[j+1],ls[j])
    return ls


