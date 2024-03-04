def solution(n, t):
    answer = n
    for i in range(t): #여기선 왜 str이나 int말고 range를 써야하는가
        answer *= 2
        
    return answer