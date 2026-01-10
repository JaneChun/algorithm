# 처리시간이 i인 코어는 시간 T까지 (T // i) + 1개 만큼 작업을 시작한다. (0초 시작하는 1개 포함)
# 이 공식을 사용해 모든 코어에 대해 합치면, T까지 시작된 전체 작업의 수를 구할 수 있다.
# T = n번째 작업이 ‘시작되는 시점’

# T = 0: 작업 시작하는 코어는 1, 2, 3
# T = 1: (1 // i) == 0을 만족하는 1
# T = 2: (2 // i) == 0을 만족하는 1, 2 -----> 시작한 작업의 개수가 6개가 되므로 T = 2

# n번째(마지막) 작업을 담당한 코어를 찾으려면?
# T초에는 여러 작업이 동시에 시작되므로, n번째 작업을 맡는 코어를 찾아야 한다.
# T-1초까지 시작된 작업을 보면
# T = 1: 4개의 작업이 시작됨
# 그렇다면 T초에는 2개가 시작된다는 뜻이므로
# T = 2: 1, 2 중 1은 5번째 작업 2는 6번째 작업에 배정됨을 알 수 있다.


def solution(n, cores):
    left = 0 # 작업이 시작될 수 있는 가장 빠른 시간
    right = max(cores) * (n - 1) # 작업이 시작될 수 있는 가장 느린 시간 (가장 느린 코어가 모든 작업을 처리하는 경우)
    
    while left < right:
        mid = (left + right) // 2
        total_started_works = 0 # mid까지 시작된 총 작업의 수
        
        for core in cores:
            total_started_works += (mid // core) + 1
        
        if total_started_works < n:
            left = mid + 1
        else:
            right = mid
    
    T = right
    
    started_works_before_T = 0 # T-1까지 시작된 총 작업의 수
    
    for core in cores:
        started_works_before_T += ((T - 1) // core) + 1
        
    started_works_T = n - started_works_before_T # T초에 시작된 작업의 수
    
    # T초에 작업을 시작한 코어들을 구하고, 그 중 started_works_T번째가 마지막 작업을 처리한 코어이다.
    avail_cores_at_T = []
    for i, core in enumerate(cores):
        if T % core == 0:
            avail_cores_at_T.append(i + 1)
    
    return avail_cores_at_T[started_works_T - 1]