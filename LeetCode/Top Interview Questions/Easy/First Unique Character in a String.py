# 문자열 s가 주어졌을 때, 반복되지 않는 첫 번째 문자를 찾아 그 문자의 인덱스를 반환하세요.
# 그런 문자가 존재하지 않으면 -1을 반환하세요.

import sys
from collections import defaultdict

input = sys.stdin.readline()

count_dict = defaultdict(lambda: {"idx": None, "count": 0})

for i in range(len(input)):
    char = input[i]
    if char in count_dict:
        count_dict[char]["count"] += 1
    else:
        count_dict[char] = {"idx": i, "count": 1}

for char, info in count_dict.items():
    idx, count = info["idx"], info["count"]
    if count == 1:
        print(idx)
        break
else:
    print(-1)
