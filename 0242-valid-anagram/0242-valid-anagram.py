class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for letter in t:
            s = s.replace(letter, "", 1)
        return not len(s)