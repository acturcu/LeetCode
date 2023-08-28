class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n < 0:
            return 1 / self.myPow(x, -n)
        else:
            if n % 2 == 0:
                k = self.myPow(x, n/2)
                return k * k
            else:
                return x * self.myPow(x, n-1)

