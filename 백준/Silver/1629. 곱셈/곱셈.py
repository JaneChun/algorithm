import sys

a, b, c = map(int, sys.stdin.readline().split(" "))

# a^b 는 a^*b/2 * a^b/2이다.
# e.g. 2^8 = 2^4 * 2^4
# e.g. 2^7 = 2^3 * 2^3 * 2
def power(a, b):
    if b == 0:
        return 1  # n^0 = 1

    half = power(a, b // 2)

    if b % 2 == 0:
        return (half * half) % c
    else:
        return (half * half * a) % c


answer = power(a, b)

print(answer)