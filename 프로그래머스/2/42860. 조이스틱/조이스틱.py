# 알파벳을 찾기 위한 최소 move (아래로 이동할지 위로 이동할지)
# 커서 위치를 변경하는 최소 move(왼쪽으로 이동할지 오른쪽으로 이동할지)
def solution(name):
    answer = 0
    
    # 알파벳 조작 횟수 먼저 계산
    for char in name:
        go_up = ord(char) - ord('A')
        go_down = 1 + ord('Z') - ord(char)
        answer += min(go_up, go_down)
    
    # 커서 이동 횟수 따로 계산
    go_straight = len(name) - 1 # 직진하기
    min_move = go_straight
    
    for i in range(len(name)):
        next_idx = i + 1
        # 다음 문자가 A일 때, 연속된 A가 끝나는 인덱스 찾기
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1

        right = i # 지금까지 오른쪽으로 이동해온 거리
        left = len(name) - next_idx # 연속된 A 이후 남은 문자까지의 거리
        
        go_back = right + min(right, left) + left
        # 돌아갈 때, 지금까지 온 방향으로 돌아갈지 반대로 갈지 짧은 쪽 선택
        
        min_move = min(min_move, go_back)
    
    answer += min_move

    return answer