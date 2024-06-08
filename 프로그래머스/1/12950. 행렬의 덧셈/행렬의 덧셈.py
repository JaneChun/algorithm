def solution(arr1, arr2):
    answer = []
    for i, arr in enumerate(arr1):
        answer.append([])
        for j, n in enumerate(arr):
            answer[i].append(arr1[i][j] + arr2[i][j])
            
    return answer