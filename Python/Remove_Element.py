# https://leetcode.com/problems/remove-element/description/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indexUpdate = 0
        for i in range(0, len(nums)):
            if nums[i]!=val:
                nums[indexUpdate] = nums[i]
                indexUpdate += 1

        return indexUpdate
