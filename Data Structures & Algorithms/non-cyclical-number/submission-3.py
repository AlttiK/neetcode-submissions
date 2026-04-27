class Solution:
    def isHappy(self, n: int) -> bool:

        def sumSquares(n):
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n = n // 10
            return res

        seen = set()
        while True:
            newNum = sumSquares(n)
            if newNum in seen:
                return False
            elif newNum == 1:
                return True
            else:
                seen.add(newNum)
            n = newNum
        