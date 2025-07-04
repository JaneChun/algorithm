# Success! Just solved Bricks Game on @HackerRank. Can you complete the challenge? https://hr.gs/bcfcaa #programming 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bricksGame' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def bricksGame(arr):
    total = [0] * (len(arr) + 1)
    
    for i in range(len(arr) - 1, -1, -1):
        total[i] = arr[i] + total[i + 1] 
    
    dp = [0] * (len(arr) + 1 + 2)
    # dp[i] = maximum score I can get from arr[i:]
    
    # suppose my friend always took best for her
    for i in range(len(arr) - 1, -1, -1):
        
        dp[i] = total[i] - min(dp[i + 1], dp[i + 2], dp[i + 3])
    
    return dp[0]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = bricksGame(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
