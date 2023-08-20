class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1
        sums = numbers[left] + numbers[right]

        while sums != target and left< right:
            if sums < target:
                left += 1
            else:
                right -= 1
            sums = numbers[left] + numbers[right]

        return [left+1, right+1]
