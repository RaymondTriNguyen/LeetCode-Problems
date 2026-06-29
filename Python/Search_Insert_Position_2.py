# https://leetcode.com/problems/search-insert-position/submissions/2050384700/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        leftIndex = 0
        rightIndex = len(nums) - 1
        while leftIndex <= rightIndex:
            middle = (leftIndex + rightIndex) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                leftIndex = middle + 1
                index = middle + 1
            else:
                rightIndex = middle - 1
            
        return index 
# Linear search O(n)
# O(log n) log2(n) if the array has 8 elements log2(8) = 3, binary search

#  [1, 3, 4, 6] , target = 5
# l = 0, h = 3, m = (l + h) // 2  = (0 + 3) // 2 = 3 // 2 = 1
# Now, middle idex element is 3, and target is 5
# 3 < 5, as middle element is less than target, target can never be found on the left half, so we ignore
# the left half and search only the right half in the next iteration
# l = m + 1 = 2, h = 3, m = (l + h) / 2 = (2 + 3) / 2 = 2
# middle element is 4, and target is 5. So target can never be found at the left. We ignore left and search only the right half
# l = m + 1 = 2 + 1 = 3, m = (l + h) // 2 = (3 + 3) // 2 = 3
# Middle element is 6 now, and the target is 5. As middle is greater than target, we need to check the left half. 
# h = m - 1 = 3 - 1 = 2, l =  3 , now l is greater than h



# [1, 2, 3, 4, 5, 6, 10, 100, 122, 204, 68], target - 50

# square root of 45
