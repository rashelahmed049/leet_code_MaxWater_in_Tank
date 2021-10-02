def maxWater(n):
    m = 0
    i=0
    j=len(n)-1
    
    while i<j:
        small = min(n[i],n[j])
        m = max(m,small*(j-1))
        if n[i]>n[j]:
            j-=1
        else:
            i+=1
    return m
l = [1,8,6,2,5,4,8,3,7]
k = maxWater(l)
print(k)