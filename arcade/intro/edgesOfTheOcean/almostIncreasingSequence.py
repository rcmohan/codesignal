def solution(sequence):
    diff1 = 0
    diff2 = 0
    l = len(sequence) - 1
    for i in range(l):
        if(sequence[i] >= sequence[i+1]):
            diff1 = diff1 + 1
        if(i < l - 1 and sequence[i] >= sequence[i+2]):
            diff2 = diff2 + 1

    return diff1 <= 1 and diff2 <= 1