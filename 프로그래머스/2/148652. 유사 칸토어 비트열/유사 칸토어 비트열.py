# 유사 칸토어 비트열의 n번째에서, [l, r] 범위 안에 있는 "1"의 개수를 구하기
def solution(n, l, r): # 2, 4, 17
    # n단계의 비트열에서, 전체 범위 [start, end] 중 [l, r] 구간 내 "1"의 개수를 구한다.
    def count_ones(n, l, r, start, end): # 2, 3, 16, 0, 24
        # 1, 3, 16, 0, 4 / 1, 3, 16, 5, 9 / 1, 3, 16, 15, 19 / 1, 3, 16, 20, 24
        # 0, 3, 16, 0, 0 / 0, 3, 16, 2, 2 / 0, 3, 16, 3, 3 ...
        
        # l, r 범위가 현재 블록과 겹치지 않으면 0 반환
        if l > end or r < start:
            return 0
        
        # base case
        # n == 0이면 항상 "1"
        # l, r 범위에 있으면 1, 아니면 0 반환
        if n == 0:
            return 1 if l <= start <= r else 0
        
        total = 0 # 현재 블록 내 "1"의 개수를 누적할 변수
        block_len = (end - start + 1) // 5 # 현재 블록(비트열)을 5개로 나눈 블록 하나의 길이 
        # n = 2일 때, (24 - 0 + 1) // 5 = 5
        # n = 1일 때, (4 - 0 + 1) // 5 = 1
        
        # 5개의 블록을 순회
        for i in range(5):
            block_start = start + i * block_len     
            block_end = block_start + block_len - 1 
            # n = 2: [0 ~ 4], [5 ~ 9], [10 ~ 14], [15 ~ 19], [20 ~ 24]
            # n = 1: [0 ~ 0], [1 ~ 1], [2 ~ 2], [3 ~ 3], [4 ~ 4]
            
            # 3번째 블록은 항상 "0"으로만 채워져 있으므로, 1이 있을 수 없음 → 스킵
            if i == 2:
                continue
        
            # 그외 n-1 단계로 재귀적으로 탐색하여 그 결과를 total에 누적
            total += count_ones(n - 1, l, r, block_start, block_end)

        return total

    # 1-based -> 0-based로 처리
    return count_ones(n, l - 1, r - 1, 0, 5 ** n - 1)