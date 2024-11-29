def solution(arr):
    answer = [0, 0] # 압축된 0의 개수와 1의 개수를 저장
    
    def compress(start_row, end_row, start_col, end_col):
        # 현재 범위의 첫 번째 값
        cur = arr[start_row][start_col]
        
        # 범위 내의 모든 값이 첫 번째 값과 같은지 확인
        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                if cur != arr[i][j]: # 값이 다르면 압축 불가
                    
                    # 배열을 4등분하여 재귀 호출
                    mid_row = (start_row + end_row) // 2
                    mid_col = (start_col + end_col) // 2
                    
                    compress(start_row, mid_row, start_col, mid_col) # 1사분면
                    compress(start_row, mid_row, mid_col, end_col) # 2사분면
                    compress(mid_row, end_row, start_col, mid_col) # 3사분면
                    compress(mid_row, end_row, mid_col, end_col) # 4사분면
                    return  # 압축 완료 후 리턴
                    
                    
        # 모든 값이 같아 반복문이 정상적으로 종료되면 해당 값을 압축
        answer[cur] += 1
    
    compress(0, len(arr), 0, len(arr))
    
    return answer