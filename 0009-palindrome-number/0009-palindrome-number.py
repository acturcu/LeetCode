class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        copy_x = x
        rev = 0
        while copy_x:
            rev *= 10
            rev += copy_x%10
            copy_x = copy_x // 10
            
        return x == rev