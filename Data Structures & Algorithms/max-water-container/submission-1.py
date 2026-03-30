class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxi = 0
        while l < r:
            amount = min(heights[l], heights[r]) * (r-l)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l, r = l+1, r-1
            if amount > maxi:
                maxi = amount
        return maxi