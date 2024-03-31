def solution(price):
    answer = 0
    if(price >= 500000):
        answer = price * 0.2
        price -= answer
    elif(price >=300000):
        answer = price * 0.1
        price -= answer
    elif(price >=100000):
        answer = price * 0.05
        price -= answer
    
        
    return int(price)