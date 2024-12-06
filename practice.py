def solution(arr):
    answer = []
    for i in arr:
        if i > 50 or i % 2 == 0 :
            answer.append(i % 2)
        else:
            answer.append(i*2)
    return answer 
print
