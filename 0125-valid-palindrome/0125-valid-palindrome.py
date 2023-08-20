class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum = ''.join(ch for ch in s if ch.isalnum())
        alphanum = alphanum.lower()

        return alphanum == alphanum[::-1]