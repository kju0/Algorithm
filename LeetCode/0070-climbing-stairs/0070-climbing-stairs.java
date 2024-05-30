import java.util.*;

class Solution {
    private Map<Integer, Integer> memo = new HashMap<>();

    public int climbStairs(int n) {
        return fibonacci(n);
    }

    private int fibonacci(int num) {
        if (num <= 3) return num;

        if (memo.containsKey(num)) return memo.get(num);

        int result = fibonacci(num - 1) + fibonacci(num - 2);

        memo.put(num, result);

        return result;
    }
}