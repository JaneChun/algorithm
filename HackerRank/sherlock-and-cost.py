# Success! Just solved Sherlock and Cost on @HackerRank. Can you complete the challenge? https://hr.gs/emf #programming 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def cost(B):
    # 1 <= A[i] <= B[i]
    # |A[i] - A[i - 1]| should be maximum
    
    dp_low = [0] * n # max_sum when A[i] is 1
    dp_high = [0] * n # max_sum when A[i] is B[i]
    
    # A[i] should be high[i] if A[i - 1] was 1
    # A[i] should be 1       if A[i - 1] was high[i - 1]
    
    for i in range(1, n):
        # 1: A[i] = 1
        # 1-1. if prev was low(1)
        # cur = 1
        # prev = 1
        diff = abs(1 - 1) # cur - prev
        low_sum_1 = dp_low[i - 1] + diff
        
        # 1-2. else if prev was high(B[i - 1])
        # cur = 1
        # prev = B[i - 1]
        diff = abs(1 - B[i - 1])
        low_sum_2 = dp_high[i - 1] + diff
        
        dp_low[i] = max(low_sum_1, low_sum_2)
        
        # 2. A[i] = B[i]
        # 2-1. if prev was low(1)
        # cur = B[i]
        # prev = 1
        diff = abs(B[i] - 1)
        high_sum_1 = dp_low[i - 1] + diff
        
        # 2-2. else if prev was high(B[i - 1])
        # cur = B[i]
        # prev = B[i - 1]
        diff = abs(B[i] - B[i - 1])
        high_sum_2 = dp_high[i - 1] + diff
        
        dp_high[i] = max(high_sum_1, high_sum_2)
    
    return max(dp_low[-1], dp_high[-1])
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
