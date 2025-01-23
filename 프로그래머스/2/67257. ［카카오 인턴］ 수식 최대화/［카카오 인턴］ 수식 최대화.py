import re

def solution(expression): # 연산자(+,-,*)의 우선순위를 재정의하여 절댓값이 가장 큰 숫자 만들기
    answer = []
    cases = [
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['-', '+', '*'],
        ['-', '*', '+'],
        ['*', '+', '-'],
        ['*', '-', '+']
    ]
    
    for case in cases: # 연산자 우선순위 배열
        tokens = re.split(r'(\D)', expression)  # 숫자가 아닌 문자 기준으로 분리
        # ['100', '-', '200', '*', '300', '-', '500', '+', '20']
        for operator in case: # 처리중인 연산자
            while operator in tokens:
                # 연산자가 있는 위치를 찾음
                op_idx = tokens.index(operator)
                
                # 연산자 앞뒤 숫자와 연산자를 추출
                a = tokens[op_idx - 1]
                b = tokens[op_idx + 1]
                
                # 계산
                calculated = eval(f"{a} {operator} {b}")

                 # tokens 리스트 업데이트: 계산된 값 반영
                tokens = tokens[:op_idx - 1] + [str(calculated)] + tokens[op_idx + 2:]      
        
        [acc_calculated] = tokens
        answer.append(abs(int(acc_calculated)))
        
    return max(answer)