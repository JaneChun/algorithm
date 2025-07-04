Success! Just solved The Maximum Subarray on @HackerRank. Can you complete the challenge? https://hr.gs/dsh #programming 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    # save the maximum sum of i in  dp[i]
    dp = [0] * len(arr)
    dp[0] = arr[0]
    
    for i in range(1, len(arr)):
        dp[i] = max(arr[i], arr[i] + dp[i - 1])
    
    subarray_sum = max(dp)
    
    subsequence_sum = sum(filter(lambda x: x > 0, arr))

    return [subarray_sum, max(arr) if subsequence_sum == 0 else subsequence_sum]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
