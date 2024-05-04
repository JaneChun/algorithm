def solution(strlist):
    def getLength(arr):
        return len(arr)
    answer = list(map(getLength, strlist)) # map 함수는 iterator를 반환하므로 이를 list로 변환
    return answer