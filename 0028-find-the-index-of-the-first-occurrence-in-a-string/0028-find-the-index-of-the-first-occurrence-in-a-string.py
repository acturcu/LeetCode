class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # for ind, char in enumerate(haystack):
        #     curr = cpy[0]
        #     if curr == char:
        #         cpy = cpy.replace(curr, '', 1)
        #         if len(cpy) == 0:
        #             return ind - len(needle) + 1
        #     else:
        #         cpy = needle
        
        if needle == haystack:
            return 0

        index = 0 
        while index <= len(haystack) - len(needle):
            if haystack[index:index+len(needle)] == needle:
                return index
            index += 1
        return -1