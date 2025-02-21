def solution(w,h):
    gcd = get_gcd(w, h)
    
    # 패턴의 가로 세로 길이
    pattern_w = w // gcd
    pattern_h = h // gcd
    pattern_count = w / pattern_w
    
    # 전체 사각형 개수 - 패턴이 차지하는 사각형 개수
    # 패턴이 차지하는 사각형 개수 규칙: 정사각형이면 x개, 직사각형이면 x + y - 1개
    unusable = 0
    if pattern_w == pattern_h:
        unusable = pattern_w
    else:
        unusable = pattern_w + pattern_h - 1
    
    return w * h - unusable * pattern_count

# 최대 공약수
def get_gcd(a, b):
    if a < b:
        a, b = b, a
        
    if b == 0:
        return a

    r = a % b
    return get_gcd(b, r)