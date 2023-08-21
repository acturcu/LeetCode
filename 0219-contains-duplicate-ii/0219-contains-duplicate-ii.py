class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # for index in range(len(nums) ):
        #     curr = nums[index]
        #     if curr in nums[index+1: index + k + 1]:
        #         return True
        
        # return False

        dictionary = {}
        for index, nr in enumerate(nums):
            if nr in dictionary and abs (dictionary[nr] - index) <= k:
                return True
            dictionary[nr] = index
        return False 