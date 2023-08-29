class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        curr = 0
        for i in range(len(nums)):
            if curr < i:
                return False
            else:
                curr = max(curr, i + nums[i])         
        return True
        