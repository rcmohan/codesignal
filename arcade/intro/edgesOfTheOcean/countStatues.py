def solution(statues):
    statues.sort()
    l = len(statues) - 1
    return sum(statues[i+1] - statues[i] - 1 for i in range(l)) if (l > 0) else 0