# 875. Koko Eating bananas
# Return the minimum integer k such that she can eat all the bananas within h hours.
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        max_trips = h / len(piles)
        left = max(min(piles) // max_trips, 1)
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2
            total_hours = sum((pile + mid - 1) // mid for pile in piles)

            if total_hours > h:
                left = mid + 1
            else:
                right = mid - 1
        return left


# 153. Find Minimum in Rotated Array
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        curr_min = float("inf")

        while l <= r:
            mid = l + (r - l) // 2
            curr_min = min(curr_min,nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
                
            # left has the  min 
            else:
                r = mid - 1 
            
        return curr_min
