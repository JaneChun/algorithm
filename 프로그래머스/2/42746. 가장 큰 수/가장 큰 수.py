# def solution(numbers):
#     sorted_numbers = bubble_sort(numbers)
#     stringified_numbers = map(str, sorted_numbers) # map(lambda x: str(x), sorted_numbers)
    
#     return ''.join(stringified_numbers)

# def bubble_sort(numbers):
#     n = len(numbers)
    
#     for i in range(n):
#         for j in range(n - i - 1): # 매번 루프가 끝날 때마다, 맨 오른쪽 값은 이미 정렬된 상태이므로 비교 범위를 i만큼 줄여야 함
#             # print(j, ' 와 ', j + 1, ' 을 비교')
#             if str(numbers[j]) + str(numbers[j + 1]) < str(numbers[j + 1]) + str(numbers[j]):
#                 # 스왑
#                 numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

#     return numbers

# 버블 정렬은 시간 복잡도가 O(n^2)이므로 O(nlogn)인 파이썬 내장 메서드 sorted() 사용하는 게 나음
def solution(numbers):
    sorted_numbers = sorted(numbers, key=lambda x: str(x)*3, reverse=True)
    stringified_numbers = list(map(str, sorted_numbers))
    
    return '0' if stringified_numbers[0] == '0' else ''.join(stringified_numbers)