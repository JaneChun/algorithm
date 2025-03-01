from itertools import combinations

def solution(relation):
    answer = 0
    row_len = len(relation[0])
    indexes = [j for j in range(row_len)]
    
    candidate_keys = []
    
    for i in range(1, row_len + 1): # 1, 2, 3, 4
        # i개의 속성으로 이루어진 후보키 찾기    
        combos = list(combinations(indexes , i))
        for combo in combos:
            if is_candidate_key(combo, relation):
                if is_minimal(combo, candidate_keys):
                    candidate_keys.append(set(combo))
                    answer += 1
    
    return answer

def is_candidate_key(combo, relation):
    row_set = set()
    
    for rel in relation:
        acc = ''
        for col in combo:
            acc += rel[col]

        if acc in row_set:
            return False
        
        row_set.add(acc)

    return True

def is_minimal(combo, candidate_keys):
    for keys in candidate_keys:
        if keys.issubset(set(combo)):  # 기존 후보키가 현재 키의 부분집합이면 최소성 만족 x
            return False
    return True
