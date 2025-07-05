# Success! Just solved Fibonacci Modified on @HackerRank. Can you complete the challenge? https://hr.gs/do1 #programming 

#!/bin/python3

import math
import os
import random
import re
import sys

sys.set_int_max_str_digits(1000000)

#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#

# t[i+2] = t[i] + t[i + 1]^2

def fibonacciModified(t1, t2, n):
    dp = [0] * (n)
    dp[0] = t1
    dp[1] = t2
    
    for i in range(2, n):
        dp[i] = dp[i - 2] + dp[i - 1] ** 2
        
    return dp[-1]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
