def solution(my_string):
    answer = ''
    c = ("a,e,i,o,u")
    for i in my_string:
        if i not in c:
            answer += i
    return answer