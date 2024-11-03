# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         num = numbers[i]
#         bigger_num = findBiggerNumber(num, numbers[i:])
#         answer.append(bigger_num)
#     return answer


# def findBiggerNumber(n, back_arr):
#     for b in back_arr:
#         if b > n:
#             return b
        
#     return -1

# 위 풀이는 시간 복잡도가 O(n^2)

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        cur = numbers[i]
        # 스택 안에 현재 숫자보다 작은 숫자가 있으면 모두 pop
        while stack and numbers[stack[-1]] < cur:
            # 스택에서 제거 & 뒷 큰수 추가
            index = stack.pop()
            answer[index] = cur
            
        stack.append(i) # 현재 인덱스를 스택에 추가
        # print(stack)
        
    return answer