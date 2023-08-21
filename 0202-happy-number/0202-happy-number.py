class Solution:
    def square(self, n: int) -> int:
        sq = 0
        while n != 0:
            digit = n%10
            sq += digit ** 2
            n = n // 10
        return sq

    def isHappy(self, n: int) -> bool:
        occured = []
        while n != 1:
            n = self.square(n)
            if n in occured:
                break
            else:
                occured.append(n)

        return n == 1
