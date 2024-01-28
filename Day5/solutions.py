# 11. Container with Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        max_vol = -1

        while l < r:
            if min(height[l],height[r]) * (r-l) > max_vol:
                max_vol = min(height[l],height[r]) * (r-l)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
                
        return max_vol
        
