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
    go_straight = len(name) - 1 # 직진하기(->)
    min_move = go_straight
    
    for i in range(len(name)):
        next_idx = i + 1
        
        # 다음 문자가 A일 때, 연속된 A가 끝나는 인덱스 찾기
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1

        go_back_then_front = (len(name) - next_idx) * 2 + i # 뒤에서 next_idx까지 이동(<-) + 끝까지 처리(->) + i로 돌아옴(->)
        go_front_then_back = i*2 + len(name) - next_idx # i까지 이동(->) + 앞으로 되돌아감(<-) + 뒤에서 next_idx까지 이동(<-)
        
        min_move = min(min_move, go_back_then_front, go_front_then_back)
        
    answer += min_move

    return answer

# "ABAAAABAA"
# i = 1
# next_idx = 6
# len(name) = 9

# go_front_then_back = 1*2 + (9 - 6) = 2 + 3 = 5
# go_back_then_front = (9 - 6)*2 + 1 = 3*2 + 1 = 6 + 1 = 7