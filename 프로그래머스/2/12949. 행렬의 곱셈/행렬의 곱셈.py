def solution(arr1, arr2):
    answer = []
    # A의 행 개수만큼 반복
    for i in range(len(arr1)): # 0 1 2
        row = []
        # B의 열 개수만큼 반복
        for j in range(len(arr2[0])): # 0 1 2
            # 행렬 곱을 계산하기 위해 값을 더해줌
            sum_val = 0
            for k in range(len(arr2)): # 0 1 2
                sum_val += arr1[i][k] * arr2[k][j]
            row.append(sum_val)
        answer.append(row)
    return answer


# 행렬 곱셈은 A의 열 개수(2)와 B의 행 개수(2)가 같을 때 가능
# 결과 행렬 C의 크기는 A의 행 수(3) * B의 열 수(2) = 3 * 2이다.

# [2, 3, 2]   [5, 4, 3]    [10 + 6 + 6, 8 + 12 + 2, 6 + 3 + 2]
# [4, 2, 4] * [2, 4, 1] =  [20 + 4 + 12, 16 + 8 + 4, 12 + 2 + 4]
# [3, 1, 4]   [3, 1, 1]    [15 + 2 + 12, 12 + 4 + 4, 9 + 1 + 4]