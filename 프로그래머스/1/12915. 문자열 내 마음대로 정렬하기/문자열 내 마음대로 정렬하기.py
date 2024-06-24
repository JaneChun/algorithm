def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
    # key 함수 : 리스트의 각 요소에 대해 호출되며, 반환값이 정렬의 기준이 됨
    # 첫 번째 요소가 동일한 경우, 두 번째 요소를 기준으로 정렬함