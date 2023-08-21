class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k >= len(nums) and len(set(nums)) != len(nums):
            return True

        for index in range(len(nums) ):
            curr = nums[index]
            if curr in nums[index+1: index + k + 1]:
                return True
        
        return False