# Success! Just solved Equal on @HackerRank. Can you complete the challenge? https://hr.gs/e4y #programming 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equal(arr):
    min_val = min(arr)
    candidates = [] # results of each diff(0 ~ 4)
    
    for diff in range(4):
      total = 0
      
      for num in arr:
        target = num - min_val + diff
        total += target // 5 + (target % 5) // 2 + (target % 5) % 2
      
      candidates.append(total)
  
    return min(candidates)      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
