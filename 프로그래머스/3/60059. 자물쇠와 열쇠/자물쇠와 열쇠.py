def rotate_90(key):
    N = len(key)
    rotated = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            rotated[j][N - 1 - i] = key[i][j]
    
    return rotated

def check(lock, key, x_offset, y_offset):
    N = len(lock)
    M = len(key)
    
    for i in range(N):
        for j in range(N):
            val = lock[i][j] # 현재 자물쇠의 값
            
            key_i = i - x_offset
            key_j = j - y_offset
            
            if 0 <= key_i < M and 0 <= key_j < M:
                val += key[key_i][key_j] # val(0) + key(1) = 1
            
            # 1이 아닌 경우, 열수 없음(0이거나 2인 경우)
            if val != 1:
                return False
    # 모두 통과한 경우 True
    return True

def solution(key, lock):
    N = len(lock)
    M = len(key)
    
    keys = [key]
    for _ in range(3):
        key = rotate_90(key)
        keys.append(key)
    
    # offset 이동
    for rotated_key in keys:
        for x_offset in range(-M + 1, N): # key의 맨 오른쪽 한칸만 포함 ~ key의 맨 왼쪽 한 칸만 포함
            for y_offset in range(-M + 1, N): # key의 맨 위 한칸만 포함 ~ key의 맨 아래 한 칸만 포함
                if check(lock, rotated_key, x_offset, y_offset):
                    return True
    return False