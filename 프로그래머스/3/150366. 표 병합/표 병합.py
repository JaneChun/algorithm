# parent 이차원 배열
# ✔ 각 셀은 처음에 자기 자신을 대표로 가짐
# ✔ 병합되면 대표 좌표가 바뀜
# ✔ 값이 어디에 저장되어 있는지 “위치 정보”를 들고 있음

# 초기 상태
# parent[1][1] = (1,1)
# parent[1][2] = (1,2)

# value[1][1] = EMPTY
# value[1][2] = EMPTY

def solution(commands):
    answer = []
    parent = [[(r, c) for c in range(51)] for r in range(51)] # “값이 어디에 있는지” 대표 좌표를 가리킴
    value = [["EMPTY" for _ in range(51)]  for _ in range(51)] # 실제 값은 “대표 셀에만” 들어감
    # 모든 명령은 find → 대표 좌표 → value 접근
    
    # 값이 있는 위치(대표 좌표)를 알려줌
    def find(r, c):
        if parent[r][c] != (r, c): # (r, c)가 대표셀이 아니라면
            parent[r][c] = find(*parent[r][c]) # 경로 압축
        
        return parent[r][c]
        
    def union(r1, c1, r2, c2):
        root_r1, root_c1 = find(r1, c1)
        root_r2, root_c2 = find(r2, c2)
        
        if (root_r1, root_c1) == (root_r2, root_c2): # 선택한 두 위치의 셀이 같은 셀일 경우 무시함
            return
        
        if value[root_r1][root_c1] != 'EMPTY': # 왼쪽 셀의 값이 우선
            parent[root_r2][root_c2] = (root_r1, root_c1)
        else:
            parent[root_r1][root_c1] = (root_r2, root_c2)
            
    def update(r, c, val):
        root_r, root_c = find(r, c) # 대표 좌표가 본인인 경우에만 value에 업데이트
        value[root_r][root_c] = val
        
    def replace(from_value, to_value):
        for i in range(51):
            for j in range(51):
                if value[i][j] == from_value:
                    value[i][j] = to_value
    
    def merge(r1, c1, r2, c2):
        union(r1, c1, r2, c2)
        
    def unmerge(r, c):
        root_r, root_c = find(r, c) # 그룹 대표 좌표 찾기
        root_value = value[root_r][root_c] # 그룹의 값 임시 저장
        
        group = []
        for i in range(51): # 모든 셀을 돌며 같은 그룹의 셀을 찾아
            for j in range(51):
                if find(i, j) == (root_r, root_c):
                    group.append((i, j))
                    
        for i, j in group:
            parent[i][j] = (i, j) # 그룹 해체
            value[i][j] = 'EMPTY' # 'EMPTY' 처리
        
        value[r][c] = root_value # r, c에만 값 복원
                    
        
    def _print(r, c):
        root_r, root_c = find(r, c)
        answer.append(value[root_r][root_c])
        
    for command in commands:
        cmd = command.split(' ')[0]
        
        if cmd == 'UPDATE':
            parts = command.split(' ')

            if len(parts) == 4:
                _, r, c, val = parts
                update(int(r), int(c), val)
            else:
                _, from_val, to_val = parts
                replace(from_val, to_val)
        elif cmd == 'MERGE':
            _, r1, c1, r2, c2 = command.split(' ')
            
            merge(int(r1), int(c1), int(r2), int(c2))
        elif cmd == 'UNMERGE':
            _, r, c = command.split(' ')

            unmerge(int(r), int(c))   
        else: # cmd == 'PRINT'
            _, r, c = command.split(' ')
            
            _print(int(r), int(c))
    
    return answer