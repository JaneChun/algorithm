# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# n개의 버전 중 가장 앞쪽의 bad version을 찾아라
# isBadVersion API 호출을 최소화하라
# 1부터 n까지 순서대로 호출하기? O(N) => 2³¹은 2,147,483,648 (약 21억 4,700만)
# 이진 탐색 O(log N) -> 탐색 횟수는 최대 31번
    # 이진 탐색은 한 번 비교할 때마다 탐색 범위를 절반으로 줄인다.
    # 2^31−1 → 2^30−1 → 2^29−1 → ⋯ → 1

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = 2**31 - 1

        while left < right:
            mid = (left + right) // 2

            # mid가 badVersion이라면 앞으로 이동
            # 이때 mid도 가장 앞에 있는 bad version일 수 있으므로 다음 탐색 범위에 포함시켜야 함
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        
        return left