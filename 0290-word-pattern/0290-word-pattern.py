class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        stringList = s.split()
        if len(pattern) != len(stringList):
            return False 
        dictionary = {}
        for index in range(len(pattern)):
            print(stringList[index])
            if pattern[index] not in dictionary.keys() :
                dictionary[pattern[index]] = stringList[index]
            
            elif dictionary[pattern[index]] != stringList[index]:
                return False
        
        return len(dictionary.values()) == len(set(dictionary.values()))
            