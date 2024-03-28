import math
def solution(n):
    answer = math.sqrt(n)
    if(answer % 1 == 0):
        return 1
    else:
        return 2
