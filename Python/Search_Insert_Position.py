// https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] < target:
                index = i+1

        return index

# Linear search O(n)
# O(log n) log2(n) if the array has 8 elements log2(8) = 3, binary search

#  [1, 3, 5, 6] , target = 5
# l = 0, h = 3, m = (l + h) / 2 = (0 + 3) / 2 = 1
# l = m + 1 = 2, h = 3, m = (l + h) / 2 = (2 + 3) / 3 = 2


# [1, 2, 3, 4, 5, 6, 10, 100, 122, 204, 68], target - 50

# square root of 45
