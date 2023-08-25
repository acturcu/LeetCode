# from os.path import commonprefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # return commonprefix(strs)
        strs.sort()
        first = strs[0]
        last = strs[-1]
        commonIndex = 0
        while commonIndex < len(first):
            if first[commonIndex] == last[commonIndex]:
                commonIndex +=1
            else: 
                break
        return first[:commonIndex]