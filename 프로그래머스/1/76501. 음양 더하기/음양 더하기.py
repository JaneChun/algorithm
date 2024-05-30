def solution(absolutes, signs):
    zipped = zip(absolutes, signs)
    print(list(zipped)) # 	[(4, True), (7, False), (12, True)]
    
    return sum(num if sign == True else -num for num, sign in zip(absolutes, signs))