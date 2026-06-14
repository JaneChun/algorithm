# 정수 배열 nums와 음이 아닌 정수 k가 주어졌을 때, 배열을 오른쪽으로 k칸만큼 회전하세요.

# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# 설명:
# 오른쪽으로 1칸 회전: [7,1,2,3,4,5,6]
# 오른쪽으로 2칸 회전: [6,7,1,2,3,4,5]
# 오른쪽으로 3칸 회전: [5,6,7,1,2,3,4]

# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# 설명:
# 오른쪽으로 1칸 회전: [99,-1,-100,3]
# 오른쪽으로 2칸 회전: [3,99,-1,-100]

# 제약 조건:
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5

# 후속 과제:
# 가능한 한 많은 풀이 방법을 생각해 보세요. 최소 세 가지 다른 방법이 있습니다.
# O(1)의 추가 공간만 사용하여 제자리에서 풀 수 있나요?

# 힌트 1:
# 가장 쉬운 풀이는 추가 메모리를 사용하는 것이며, 그것도 전혀 문제 없습니다.

# 힌트 2:
# 진짜 묘미는 추가 메모리를 전혀 사용하지 않고 이 문제를 풀려고 할 때 나옵니다.
# 즉, 원본 배열을 활용해서 원소들을 옮겨야 한다는 뜻입니다. 각 원소를 원래 있어야 할
# 위치에 놓고 그 주변의 모든 원소를 밀어서 맞추는 방식은 비용이 너무 크고, 큰 입력
# 배열에서는 시간 초과가 날 가능성이 높습니다.

# 힌트 3:
# 한 가지 접근은 배열(또는 배열의 일부)을 뒤집어서 원하는 결과를 얻는 것입니다.
# 예시를 가지고, 뒤집기(reversal)가 어떻게 우리를 도와줄 수 있는지 생각해 보세요.

# 힌트 4:
# 다른 접근은 조금 더 복잡하지만, 본질적으로 각 원소를 원래 위치에 놓으면서
# 그 위치에 원래 있던 원소를 따로 기억해 두는 아이디어에 기반합니다. 즉, 매 단계마다
# 한 원소를 제자리에 놓고, 이미 그 자리에 있던(덮어쓰이는) 원소를 추가 변수에 보관합니다.
# 이것은 한 번의 선형 순회로는 할 수 없으며, 원소들 간의 순환 의존성(cyclic-dependency)에
# 기반한 아이디어입니다.

# =================================================
# 1. 시간복잡도 O(N), 공간복잡도 O(N)의 풀이

# import sys
# input = sys.stdin.readline

# nums = list(map(int, input().split(",")))
# k = int(input())

# original = nums[:]

# for i in range(len(nums)):  # 0 1 2 3 4 5 6 -> 3 4 5 6 0 1 2
#     new_idx = (i + k) % len(nums)
#     nums[new_idx] = original[i]

# print(",".join(map(str, nums)))

# =================================================
# 2. 뒤집기(reversal) 풀이

# import sys
# input = sys.stdin.readline

# nums = list(map(int, input().split(",")))
# k = int(input())

# k = k % len(nums)

# nums.reverse()  # 7, 6, 5, 4, 3, 2, 1
# nums[0:k] = reversed(nums[0:k])
# nums[k:] = reversed(nums[k:])

# print(",".join(map(str, nums)))
# 시간복잡도: O(N) + O(K) + O(N-K) = O(2N) = O(N)

# =================================================
# 3. 순환 의존성(cyclic-dependency) 방식

import sys

input = sys.stdin.readline

nums = list(map(int, input().split(",")))
k = int(input())

n = len(nums)
k = k % n
count = 0  # 자리가 확정된 원소 개수
start_idx = 0  # 현재 사이클의 출발 인덱스

while count < n:  # 모든 원소가 자리가 확정될 때까지 반복
    cur_idx = start_idx
    cur = nums[start_idx]
    # print("[DEBUG]", "start_idx", start_idx)

    while True:
        next_idx = (cur_idx + k) % n  # 현재값이 가야할 위치

        cur, nums[next_idx] = nums[next_idx], cur  # 스왑

        cur_idx = next_idx  # 현재값 갱신
        count += 1

        if cur_idx == start_idx:  # 출발점으로 돌아오면 한 사이클 끝
            break
        # print("[DEBUG] nums", nums, "cur", cur)

    start_idx += 1  # 다음 사이클 시작

print(",".join(map(str, nums)))
