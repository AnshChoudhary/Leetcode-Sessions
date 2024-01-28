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
        
# 42. Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(height[l], maxL)
                res += (maxL - height[l])
            else:
                r -= 1
                maxR = max(height[r], maxR)
                res += (maxR - height[r])
        
        return res

# 22. Generate Parenthesis
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        "()"
        "(())", "()()"
        "((()))","(()())","(())()","()(())","()()()"

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0,0)
        return res
            
