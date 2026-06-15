# 오름차순 정렬된 정수 배열
# 합이 target이 되는 두 숫자를 찾아라
# 1 <= a <= b <= len
# 두 숫자의 인덱스를 [i, j]로 리턴하라 (1-based index)
# 메모리는 상수 O(1)? 만큼 사용해야 한다
# 입력값이 3 * 10^4 까지므로 O(N^2) = 900,000,000은 9초 걸리므로 안됨
# 투포인터 사용하면 O(N)으로 풀 수 있음
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            print('left', left, 'right', right)
            sum = numbers[left] + numbers[right]

            if sum == target:
                print('sum == target', sum)
                return [left + 1, right + 1] # 1-based-index
            elif sum < target:
                print('sum < target', sum)
                print('left += 1')
                left += 1
            else:
                print('sum > target', sum)
                print('right -= 1')
                right -= 1