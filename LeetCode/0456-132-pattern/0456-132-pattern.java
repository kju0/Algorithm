import java.util.*;

class Solution {
    public boolean find132pattern(int[] nums) {
        Stack<Integer> stk = new Stack<> ();
        int pop_val = Integer.MIN_VALUE;

        for (int i=nums.length-1; i >= 0; i--) {
            //stack 비어있는지 검사
            if (stk.empty()) {
                stk.push(nums[i]);
                continue;
            }

            //stack에 값이 있다면 확인
            if (stk.peek() < nums[i]) {
                while (!stk.empty()){
                    if (stk.peek() >= nums[i]) break;
                    pop_val = stk.pop();
                }
                stk.push(nums[i]);
            } else {
                if (pop_val > nums[i]) {
                    return true;
                } else {
                    stk.push(nums[i]);
                }                
            }
        }
        return false;
    }
}