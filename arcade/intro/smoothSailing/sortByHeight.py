def solution(a):
    b = list(filter(lambda x: x >= 0, a))
    b.sort()
    j = 0
    for i in range(len(a)):
        if a[i] >= 0:
            a[i] = b[j]
            j += 1
    return a
    
    
#    l = sorted([i for i in a if i > 0])
#    for n,i in enumerate(a):
#       if i == -1:
#           l.insert(n,i)
#    return l
