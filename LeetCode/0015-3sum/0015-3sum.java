import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        HashSet<ArrayList<Integer>> result_set = new HashSet<> ();
        
        int target, start, end, mid;
        target = start = end = 0;

        Arrays.sort(nums);

        for (int i=0; i<nums.length-2; i++) { //투포인터
            target = nums[i];
            
            start = i+1;
            end = nums.length-1;
            
            while (start < end) {
                int sum = target + nums[start] + nums[end];
                if (sum == 0) {
                    ArrayList<Integer> array = new ArrayList<>(Arrays.asList(target, nums[start], nums[end]));
                    result_set.add(array);
                    start++;
                    end--;
                } else if (sum < 0) {
                    start++;
                } else {
                    end--;
                }
            }
        }
        List<List<Integer>> resultList = new ArrayList<>(result_set);
        return resultList;
    }
}


