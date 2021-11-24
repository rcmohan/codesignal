
def solution(inputArray):
    maxSize = max(len(inputArray[i]) for i in range(len(inputArray)))
    return list(filter(lambda x: (len(x) == maxSize), inputArray))
