class Solution {
    public int[] searchRange(int[] nums, int target) {
        int start, end, mid;
        int [] answer = {-1, -1};

        start = mid = 0;
        end = nums.length - 1;
        while (start <= end) {
            mid = (start + end)/2;

            if (nums[mid] < target) start = mid + 1;
            else end = mid - 1;            
        }

        // Check if the target is present in the array
        if (start >= nums.length || nums[start] != target) {
            return answer;
        }

        answer[0] = start;

        end = nums.length - 1;
        while (start <= end) {
            mid = (start + end)/2;
            
            if (nums[mid] > target) end = mid - 1;    
            else start = mid + 1;
        }
        
        answer[1] = end;
        return answer;
    }
}