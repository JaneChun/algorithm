def solution(n):
    answer = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            print(i)
            answer += 1
    return answer + 1