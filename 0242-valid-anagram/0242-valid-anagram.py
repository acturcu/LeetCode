class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq = [0] * 26
        for letter in s:
            freq[ord(letter) - 97] += 1
        
        for letter in t:
            freq[ord(letter) - 97] -= 1
        
        for el in freq:
            if el:
                return False
        

        return True

            