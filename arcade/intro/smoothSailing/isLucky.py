def solution(n):
    a = [int(i) for i in str(n)]
    half = int(len(a) / 2)
    return sum(a[:half]) == sum(a[half:])


# a = map(int,str(n))