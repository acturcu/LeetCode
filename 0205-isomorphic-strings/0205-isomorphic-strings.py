class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictionary = {}
        for index in range(len(s)):
            if s[index] in dictionary:
                if dictionary[s[index]] != t[index]:
                    return False
            else:
                dictionary[s[index]] = t[index]

        return len(dictionary) == len(set(dictionary.values()))