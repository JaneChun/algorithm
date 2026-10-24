class Solution:
    def countAndSay(self, n: int) -> str:
        string = "1"

        for i in range(n - 1):
            result = []
            prev = string[0]
            count = 1
            for j in range(1, len(string)):
                cur = string[j]
                if prev == cur:
                    count += 1
                else:
                    result.append(str(count) + prev)
                    prev = cur
                    count = 1
            result.append(str(count) + prev) # 마지막 처리

            string = ''.join(result)
        
        return string