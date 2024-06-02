class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> sumCount = new HashMap<>();
        sumCount.put(0, 1);  // 초기값: sum이 0인 경우가 1번 존재

        int sum = 0;
        int count = 0;

        for (int num : nums) {
            sum += num;

            if (sumCount.containsKey(sum - k)) {
                count += sumCount.get(sum - k);
            }

            sumCount.put(sum, sumCount.getOrDefault(sum, 0) + 1);
        }

        return count;       
    }
}