def solution(phone_book):
    # 먼저 리스트를 정렬
    phone_book.sort()
    
    # 정렬된 리스트에서 인접한 전화번호만 비교
    for i in range(len(phone_book) - 1):
        # 인접한 번호들이 접두어 관계에 있는지 확인
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True
