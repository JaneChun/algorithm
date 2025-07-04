def solution(A, B):
    count = 0
    
    A.sort(reverse=True) # 7531
    B.sort(reverse=True) # 8622
    
    idx = 0
    
    for i in range(len(A)):
        # 가장 센 선수끼리 먼저 겨루게 하고
        # 지는 경우(턴을 버리는 의미) 가장 약한 선수를 출전시킨다.
        if A[i] < B[idx]:
            count += 1
            idx += 1
        else:
            B.pop()
            
    return count