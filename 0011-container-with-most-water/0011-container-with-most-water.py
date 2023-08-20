class Solution:
    def maxArea(self, height: List[int]) -> int:
        # (indexR - indexL) * min(height[indexR], height[indexL])
        if len(height) == 2:
            return min(height[0], height[1]) 
        
        indexL = 0
        indexR = len(height) - 1
        maxA = (indexR - indexL) * min(height[indexR], height[indexL])

        while indexL < indexR:
            if height[indexL] < height[indexR]:
                indexL += 1
            else: 
                indexR -= 1
            
            maxA = max(maxA, (indexR - indexL) * min(height[indexR], height[indexL]))
            
        
        return maxA