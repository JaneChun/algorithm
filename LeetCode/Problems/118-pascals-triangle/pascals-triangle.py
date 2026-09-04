# [1],         i = 0  [0]
# [1,1],       i = 1  [0,1]
# [1,2,1],     i = 2  [0,1,2]
# [1,3,3,1],   i = 3  [0,1,2,3]
# [1,4,6,4,1]  i = 4  [0,1,2,3,4]

# i 만큼 요소의 개수가 있고,
# 0번째와 n번째는 1이다,
# 1번째 ~ n-1번째는 이전 배열의 값을 더해야하는데
# n = 4이고 1번째를 구하려면 n = 3인 배열의 0번째와 1번째를 더한다.
#          2번째를 구하려면 n = 3인 배열의 1번째와 2번째를 더한다.
#          k번째를 구하려면 n = 3인 배열의 k-1번째와 k번째를 더한다.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = []
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    prev_row = result[i - 1]
                    row.append(prev_row[j-1] + prev_row[j])
            result.append(row)
        
        return result
        
        