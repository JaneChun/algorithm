# 행 또는 열을 뒤집어 목표 상태가 되기 위한 최소 횟수 구하기

# 핵심 아이디어
# - 각 행은 뒤집거나(1) 뒤집지 않거나(0) 두 가지 상태만 가진다.
# - n개의 행에 대해 가능한 경우의 수는 2^n (n ≤ 10 → 최대 1024)
# - 행 뒤집기 상태가 정해지면, 각 열을 뒤집을지 여부는 아래 조건에 의해 자동으로 결정된다.
# beginning[i][j] ⊕ rowFlip[i] ⊕ colFlip[j] = target[i][j]

# - 따라서 열의 경우의 수는 따로 탐색할 필요 없이, 모든 행 뒤집기 조합(2^n)만 검사하면 된다.
# 각 조합에서 열 뒤집기가 모순 없이 결정되면, (행 뒤집기 횟수 + 열 뒤집기 횟수)의 최소값을 갱신한다.

def solution(beginning, target):
    n = len(beginning)
    m = len(beginning[0])
    answer = float('inf')
    
    # 행 뒤집기 상태를 비트마스크로 표현
    # mask의 i번째 비트가 1이면 i번째 행을 뒤집는다.
    for mask in range(1 << n): # 0 ~ 2^n - 1
        rowFlip = [0] * n
        
        # 현재 mask에 따라 각 행의 뒤집기 여부 결정
        for i in range(n):
            if mask & (1 << i):
                rowFlip[i] = 1
                
        colFlip = [-1] * m # 각 열 뒤집기 상태(아직 미정)
        valid = True
        
        # 모든 칸을 순회하며 열 뒤집기 상태를 결정
        for i in range(n):
            for j in range(m):
                # 이 칸을 target과 맞추기 위한 열 뒤집기 여부
                need = beginning[i][j] ^ rowFlip[i] ^ target[i][j]
                
                if colFlip[j] == -1:
                    colFlip[j] = need # 이 열을 처음 만남 → 상태 확정
                elif colFlip[j] != need:
                    valid = False # 같은 열에서 다른 요구가 나오면 모순 발생
                    break
                    
            if not valid:
                break
                    
        # 모순 없이 target을 만들 수 있는 경우
        if valid:
            count = sum(rowFlip) + sum(colFlip)
            answer = min(answer, count)
    
    return -1 if answer == float('inf') else answer


# 비트이동연산자 <<
# 1 << n  =  1을 왼쪽으로 n칸 이동
# 1 << 1 = 0001 → 0010 (2)
# 2 << 1 = 0010 → 0100 (4)
# 1 << n = 2ⁿ
# range(1 << n) = 0부터 2^n - 1까지


# for mask in range(1 << n):
# n = 10이라면 0000000000(0, 아무행도 안 뒤집음) ~ 1111111111(1023, 모든 행을 뒤집음) 의 조합을 모두 시도


# for i in range(n): # mask = 6(110)
    # if mask & (1 << i):
        # 1 << i: i번째만 비트인 1인 숫자를 만들어 mask의 i번째 비트를 검사
            # i = 0: 1 << 0 = 001 → if 110 & 001 = 000(False)
            # i = 1: 1 << 1 = 010 → if 110 & 010 = 010(True)
            # i = 2: 1 << 2 = 100 → if 110 & 100 = 100(True)
        # rowFlip[i] = 1 # 즉, mask에서 i번째 행이 1이라면, i번째 행을 뒤집는다
        

# XOR(배타적 논리합)는 두 값이 다르면 1, 같으면 0
# need = beginning[i][j] ^ rowFlip[i] ^ target[i][j]
    # beginning[i][j] : 현재 동전 상태 (0 or 1)
    # rowFlip[i] : i번째 행을 뒤집었는지 (0 or 1)
    # target[i][j] : 목표 상태 (0 or 1)
    # need == 0: 이미 목표와 일치
    # need == 1: 열을 한 번 뒤집어야 목표와 일치

