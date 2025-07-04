# Success! Just solved Construct the Array on @HackerRank. Can you complete the challenge? https://hr.gs/k4cm #programming

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#

def countArray(n, k, x):
    MOD = 10 ** 9 + 7
    a = [0] * n
    b = [0] * n
    
    a[0] = 1 if x == 1 else 0 # number of cases when i ends with 'x'
    b[0] = 0 if x == 1 else 1 # number of cases when i doesn't end with 'x'
    
    for i in range(1, n):
      a[i] = b[i - 1] % MOD
      b[i] = (a[i - 1] * (k - 1) + b[i - 1] * (k - 2)) % MOD
      
    return a[n - 1]
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
