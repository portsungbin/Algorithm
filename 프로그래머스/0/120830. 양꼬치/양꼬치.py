def solution(n, k):
    s = n // 10
    answer = 0
    answer1 = 0
    answer2 = 0
    yang = 12000
    umm = 2000
    answer1 = n * yang
    answer2 = umm * (k-s)
    answer = answer1 + answer2
        
    return answer
