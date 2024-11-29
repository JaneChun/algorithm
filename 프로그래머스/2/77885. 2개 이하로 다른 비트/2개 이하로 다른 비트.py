def solution(numbers):
    return [f(x) for x in numbers]

def f(x):
    if x % 2 == 0:
        return x + 1
    
    binary_x = str(bin(x)[2:])
    if binary_x[0] == '1':
        binary_x = '0' + binary_x
        
    r_0_idx = binary_x.rfind('0')
    
    # 문자열 수정
    binary_y = binary_x[:r_0_idx] + '10' + binary_x[r_0_idx + 2:]
    
    return int(binary_y, 2)
    
    

# 홀수인 경우 규칙 : 가장 오른쪽의 0을 1로 바꾸고 (0011 -> 0111) 그 오른쪽의 1을 0으로 바꾼다 (0111 -> 0101)
# 0011 : 3
# 0100 : 4
# 0101 : 5 <--!
# 0110 : 6
# 0111 : 7


    
# brute force : 입력 범위가 크므로 시간 초과 발생
# def f(x):
#     y = x
#     while True:
#         y += 1
#         xor_result = bin(x ^ y)[2:] # XOR 연산 : num1 ^ num 2 (이진수에서 같으면 0 다르면 1 반환)
#         if str(xor_result).count('1') <= 2:
#             break
            
#     return y