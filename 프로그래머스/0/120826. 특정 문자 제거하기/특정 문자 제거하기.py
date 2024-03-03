def solution(my_string, letter):
        answer = ''
        strr = list(my_string)
        
        for i in strr[:]:
            if i == letter:
                strr.remove(letter)
                print(strr)
        answer = ''.join(strr)
        return answer