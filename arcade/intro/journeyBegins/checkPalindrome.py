def solution(inputString):
    l = len(inputString)
    m = int((l) / 2)
    n = m - 1 if(l % 2 == 0) else m 
    return inputString[:m:1] == inputString[l:n:-1]
