def solution(s):
    numDic = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    
    for word, number in numDic.items():
        s = s.replace(word, str(number))
    return int(s)


# import re

# def solution(s):
#     numArr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#     for i in range(len(numArr)):
#         num = numArr[i]
#         pattern = rf"{num}"
#         match = re.findall(pattern, s)
        
#         if match:
#             replacedS = re.sub(pattern, str(i), s)
#             s = replacedS
            
#     return int(s)
            