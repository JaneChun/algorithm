def solution(p):
    if is_right(p):
        return p
    
    # 1
    if p == '':
        return ''
    
    # 2
    u, v = get_u_v(p)

    # 3
    if is_right(u):
        return u + solution(v)
    # 4
    else: 
        return '(' + solution(v) + ')' + reverse_bracket(u[1:-1])


def is_balanced(str):
    return str.count('(') == str.count(')')

def get_u_v(p):
    for i in range(1, len(p) + 1):
        sliced = p[0 : i]
        if is_balanced(sliced):
            u = sliced
            v = p[i:]
            return [u, v]
        
def is_right(p):
    stack = []
    for b in p:
        if b == '(':
            stack.append(b)
        else:
            if stack:
                stack.pop()
    return len(stack) == 0

def reverse_bracket(u):
    return ''.join(['(' if b ==')' else ')' for b in u])