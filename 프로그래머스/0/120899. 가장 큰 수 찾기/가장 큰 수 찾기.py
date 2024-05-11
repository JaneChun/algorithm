def solution(array):
    return [max(array), array.index(max(array))];
#     max_value = max(array)
    
#     for idx, num in enumerate(array):
#         if num == max_value:
#             return [num, idx]