import java.util.*;

class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        List<Integer> prf_sum = new ArrayList<>();
        int sum = 0;
        int left =0;
        int answer = Integer.MAX_VALUE;
        for (int idx=0; idx<nums.length; idx++) {
            sum += nums[idx];

            while (sum >= target) {
                answer = Math.min(answer, idx-left+1);
                sum -= nums[left];
                left++;
            }
        }
        return (answer == Integer.MAX_VALUE ? 0 : answer); 
    }
}