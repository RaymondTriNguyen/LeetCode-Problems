// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution {
    public int removeDuplicates(int[] nums) {
        int indexUpdate = 1;

        for(int i = 1; i < nums.length; i++){
            if(nums[i] != nums[i - 1]){
                nums[indexUpdate] = nums[i];
                indexUpdate++;
            }
        }

        return indexUpdate;
    }
}
