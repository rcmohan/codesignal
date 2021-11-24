from collections import deque

def solution(inputString):
    stack = deque()
    s = ""
    for i in inputString:
        if(i == '('):
            stack.append(s)
            s = ""
        elif (i == ')'):
            s = s[len(s)::-1]
            s1 = stack.pop()
            s = s1 + s
        else:
            s += i
    return s

# Best solution
#     return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')
