class Solution:
    def isTrionic(self, nums):
        n = len(nums)
        i = 0

        # First: strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        p = i
        if p == 0 or p == n - 2 or p == n - 1:
            return False

        # Second: strictly decreasing
        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1

        q = i
        if q == p or q == n - 1:
            return False

        # Third: strictly increasing
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return i == n - 1