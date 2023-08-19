class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for character in magazine:
            ransomNote = ransomNote.replace(character,"", 1)

        return len(ransomNote) == 0