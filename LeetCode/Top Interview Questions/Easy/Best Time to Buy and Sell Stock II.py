# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/strings/564/

# 정수 배열 prices가 주어집니다. prices[i]는 i번째 날의 주식 가격입니다.
#
# 매일 주식을 사거나 팔 수 있습니다.
# 단, 한 번에 최대 1주만 보유할 수 있습니다.
# 같은 날에 팔고 다시 사는 것도 가능하지만, 보유 주식이 1주를 넘으면 안 됩니다.
#
# 얻을 수 있는 최대 이익을 구하여 반환하세요.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# 설명: 2일차에 사고(가격 = 1) 3일차에 팔면(가격 = 5) 이익 = 4.
#       4일차에 사고(가격 = 3) 5일차에 팔면(가격 = 6) 이익 = 3.
#       총 이익 = 4 + 3 = 7.

# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# 설명: 1일차에 사고(가격 = 1) 5일차에 팔면(가격 = 5) 이익 = 4.
#       총 이익 = 4.

# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# 설명: 양의 이익을 낼 수 있는 방법이 없으므로, 주식을 사지 않아 최대 이익은 0입니다.

# 제약 조건:
# 1 <= prices.length <= 3 * 10^4
# 0 <= prices[i] <= 10^4

# 접근법: 그리디

# 주식을 안가지고 있는 경우
# 오늘 사기 vs 내일 사기 비교해서 저렴할 때 산다.
# 주식을 가지고 있는 경우
# 오늘 팔기 vs 내일 팔기를 비교해서 오늘 파는게 이득이면 오늘 팔고, 내일 파는게 이득이면 가지고 있는다.

# 시간 복잡도: O(N)

import sys

input = sys.stdin.readline

arr = list(map(int, input().split(",")))

stock = None
profit = 0

for i in range(0, len(arr) - 1):
    today_price = arr[i]
    tommor_price = arr[i + 1]

    if stock is None:
        if today_price < tommor_price:
            stock = today_price
        else:
            continue
    else:
        if tommor_price < today_price:
            profit += today_price - stock
            stock = None
        else:
            continue

# 마지막날까지 가지고 있었다면 팔기
if stock is not None:
    profit += arr[-1] - stock

print(profit)
