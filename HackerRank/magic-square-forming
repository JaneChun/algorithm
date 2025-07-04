# Keep your coding skills sharp by solving programming challenges https://hr.gs/bedcab  on @HackerRank #programming 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def get_all_magic_squares():
    rotated = []
    square = [[2,7,6], [9,5,1], [4,3,8]]
  
    # rotate 4 times and get 4 magic squares
    for i in range(4):
        new_square = [[0] * 3 for _ in range(3)]
    
        for r in range(3):
            for c in range(3):
                new_square[r][c] = square[c][3 - 1 - r]
        
        rotated.append(new_square)    
        square = new_square
   
    flipped =[]
    
    # flip horizontally
    for magic_square in rotated:
        new_square = [[0] * 3 for _ in range(3)]
        
        for r in range(3):
            for c in range(3):
                if c == 1:
                    new_square[r][c] = magic_square[r][c] 
                new_square[r][c] = magic_square[r][3 - 1 - c]
        
        flipped.append(new_square)
        
    return rotated + flipped
                    
        
    
      
def formingMagicSquare(s):
  cost_arr = []
  
  magic_squares = get_all_magic_squares()
  
  for ms in magic_squares:
    cost = 0
    for r in range(3):
        for c in range(3):
            if ms[r][c] != s[r][c]:
                cost += abs(ms[r][c] - s[r][c])
                
    cost_arr.append(cost)
    
  return min(cost_arr)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
