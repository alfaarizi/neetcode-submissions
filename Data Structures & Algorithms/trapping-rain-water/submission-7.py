class Solution:
    def trap(self, height: List[int]) -> int:
        # i, j = 0, 0
        # amount = 0
        # n = len(height)
        # while i < n:
        #     if height[i] > 0:
        #         j = i+1
        #         tmp = 0
        #         while j < n and height[j] < height[i]:
        #             tmp += height[j]
        #             j += 1
        #         if j < n:
        #             amount += min(height[i], height[j]) * (j - i - 1) - tmp
        #         i = j
        #     else:
        #         i += 1
        # return amount

        # n = len(height)
        # pref, suff = [0]*n, [0]*n
        # pref[0] = height[0]
        # for i in range(1, n):
        #     pref[i] = max(pref[i-1], height[i])
        # suff[n-1] = height[n-1]
        # for i in range(n-2, -1, -1):
        #     suff[i] = max(suff[i+1], height[i])
        # amount = 0
        # for i in range(n):
        #     amount += min(pref[i], suff[i]) - height[i]
        # return amount

        n = len(height)
        l, r = 0, n-1
        max_l, max_r = height[l], height[r]
        amount = 0
        while l < r:
            if height[l] <= height[r]:
                max_l = max(height[l], max_l)
                amount += max_l - height[l]
                l += 1
            else:
                max_r = max(height[r], max_r)
                amount += max_r - height[r]
                r -= 1
        return amount





        
