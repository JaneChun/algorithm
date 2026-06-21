# n 개의 바나나 더미가 있다. i번째 더미는 piles[i] 개의 바나나를 가졌다.
# 가드가 떠났고 h시간 후에 돌아온다.
# 코코는 시간당 k개의 바나나를 먹을 수 있고,
# 더미에 k개 미만인 경우 해당 더미를 다 먹고, 남은 hour 동안은 안먹는다.
# 가드가 돌아오기 전에 모든 바나나를 다 먹어야 한다.
# 코코가 h시간 안에 모든 바나나를 다 먹을 수 있는 최소 속도 k를 찾아라.
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right =  max(piles)

        while left < right:
            time = 0
            k = (left + right) // 2
            for bananas in piles:
                # 현재 더미를 먹는데 걸리는 시간 (바나나 개수 // 시간당 먹을 수 있는 바나나 개수 k)
                t = bananas // k
                bananas = bananas % k
                time += t
                if bananas: # 나머지 처리
                    time += 1
                
            # 가드가 돌아오기 전 다 먹은 경우, 속도(k)를 줄여서 다시 테스트
            if time <= h:
                right = k
            else: # 가드가 돌아오기 전 다 못 먹은 경우, 속도를 늘려서 다시 테스트
                left = k + 1
                
        return left