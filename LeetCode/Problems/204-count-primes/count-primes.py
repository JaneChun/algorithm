# 에라토스테네스의 체
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        seive = [True for i in range(n)]
        seive[0] = seive[1] = False

        # i를 √n까지만 확인하는 이유는, 어떤 합성수 n이 있다면 반드시 √n 이하의 약수를 하나 갖기 때문이다.
        # 100 이하의 합성수는 반드시 2, 3, 5, 7 같은 10 이하의 약수를 가지고 있다.
        for i in range(2, int(math.sqrt(n)) + 1):
            if seive[i]: # 소수가 아니라면 다른 숫자를 나눌 필요가 없다.
                # i로 나눠지는 모든 수를 지운다. e.g. i = 5라면 25, 30, 35 ... 를 지운다. (10, 15, 20은 이미 i = 2, i = 3에서 지워짐)
                for j in range(i*i, n, i):
                    seive[j] = False
        
        primes = list(filter(lambda x: x == True, seive))
        
        return len(primes)
        