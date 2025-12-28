# n 레벨의 포화이진트리의 노드의 수는 2^n - 1개 (1, 3, 7, 15, 31, 63...)
# 중위순회: 왼쪽 서브트리 -> 루트 -> 오른쪽 서브트리 순서로 방문

# 7 -> 111
# 위치: 1 2 3
# 비트: 1 1 1 (3비트)
#  1
# 1 1
# => 포화이진트리이므로 True

# 42 -> 101010
# 위치: 1 2 3 4 5 6 7
# 비트: 0 1 0 1 0 1 0 (6비트는 포화이진트리가 안되므로 앞에 0을 붙여 7비트로)
#     1
#  1    1
# 0 0  0 0
# => 포화이진트리이므로 True

# 5 -> 101
# 위치: 1 2 3
# 비트: 1 0 1
#  0
# 1 1
# => 루트가 0인 트리는 유효하지 않으므로 False

# 95 -> 1011111
# 위치: 1 2 3 4 5 6 7
# 비트: 1 0 1 1 1 1 1
#     1
#  0    1
# 1 1  1 1
# => 루트가 0인 트리는 유효하지 않으므로 False

# 체크해야할 조건
# 1. 2진수로 변환한 길이가 2^n - 1인지
#   1-1. 아닌 경우 0으로 패딩
# 2. 트리가 유효한지 (부모가 0인데 자식이 있는 경우)

def int_to_binary(integer):
    return bin(integer)[2:]

def add_padding(binary):
    i = 1
    target_len = 1
    cur_len = len(binary)
    
    while True:
        target_len = 2 ** i - 1 # 1, 3, 7, 15, 31...
        if cur_len <= target_len:
            break
        i += 1
    
    padding_len = target_len - cur_len
    
    return '0' * padding_len + binary # 포화이진트리로 만들기 위해 부족한 개수만큼 0을 더해서 반환
    
# 이진수, 시작 idx, 마지막 idx를 받아 재귀적으로 올바른 트리인지 검증하는 함수
def is_valid_tree(binary, start, end):
    # 재귀함수 종료조건
    if start > end: # 범위가 유효하지 않은 경우
        return True
    
    if start == end: # 리프노드인 경우: 검증 필요 X
        return True
    

    # print(f"호출: start={start}, end={end}")
    
    # 현재 루트 찾기
    mid = (start + end) // 2
    root = binary[mid]
    
    # 현재 노드 검증
    if root == '0': # 부모(루트)가 0인데 자식 서브트리에 1이 있으면 유효하지 않은 트리
        if has_one(binary, start, end):
            return False    
    
    # 왼쪽/오른쪽 서브트리 재귀적으로 검증
    is_left_subtree_valid = is_valid_tree(binary, start, mid - 1)
    if_right_subtree_valid = is_valid_tree(binary, mid + 1, end)
    
    return is_left_subtree_valid and if_right_subtree_valid

def has_one(binary, start, end):
    return binary[start:end + 1].find('1') != -1
    
def solution(numbers):
    answer = []

    for number in numbers:
        if number == 0: # 0 예외처리
            answer.append(0)
            continue
            
        binary = int_to_binary(number)
        
        # 1번 조건
        binary = add_padding(binary)
        
        # 2번 조건
        if is_valid_tree(binary, 0, len(binary) - 1):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer