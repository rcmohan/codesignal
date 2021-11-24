def solution(inputArray):
    max = inputArray[0] * inputArray[1]
    for i in range(1, len(inputArray) - 1):
        n = inputArray[i] * inputArray[i+1]
        max = n if (max < n) else max
    
    return max

# Shortest solution max on a loop
def solution2(ia):
    return max([ia[i] * ia[i+1] for i in range(len(ia)-1)])