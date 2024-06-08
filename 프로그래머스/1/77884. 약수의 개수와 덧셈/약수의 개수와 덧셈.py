def solution(left, right):
    sum = 0
    for i in range(left, right + 1):
        # 약수의 개수가 홀수인 경우는 제곱수인 경우밖에 없음
        if (i ** 0.5 == int(i ** 0.5)):
            sum -= i
        else:
            sum += i
    return sum

# def solution(left, right):
#     sum = 0
#     for i in range(left, right + 1):
#         numOfDivisor = getDivisor(i)
#         if (numOfDivisor % 2 == 0):
#             sum += i
#         else:
#             sum -= i
#     return sum

# def getDivisor(n):
#     numOfDivisor = 0
#     for i in range(1, n + 1):
#         if (n % i == 0):
#             numOfDivisor += 1
#     return numOfDivisor