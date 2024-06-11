class Solution {
    public int removeElement(int[] nums, int val) {
        int lt = 0;

        for (int rt = 0; rt < nums.length; rt++) {
            if (nums[rt] != val) {
                nums[lt] = nums[rt];
                lt++;
            }
        }
        
        return lt;
    }
}