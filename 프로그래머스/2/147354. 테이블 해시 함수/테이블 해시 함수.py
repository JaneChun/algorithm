from functools import reduce

def solution(data, col, row_begin, row_end):
    # col번째 컬럼의 값을 기준으로 오름차순 -> 첫 번째 컬럼의 값으로 내림차순
    sorted_data = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    
    # S_i를 i 번째 행의 튜플에 대해 각 컬럼의 값을 i 로 나눈 나머지들의 합으로 정의
    all_S_i = []
    for i in range(len(sorted_data)):
        S_i = 0
        for j in sorted_data[i]:
            S_i += j % (i + 1)
        all_S_i.append(S_i)
    
    # row_begin ≤ i ≤ row_end 인 모든 S_i를 누적하여 bitwise XOR 한 값을 해시 값으로서 반환
    acc_S_i = all_S_i[row_begin - 1:row_end]
    result = reduce(lambda x, y: x ^ y, acc_S_i)
        
    return result
