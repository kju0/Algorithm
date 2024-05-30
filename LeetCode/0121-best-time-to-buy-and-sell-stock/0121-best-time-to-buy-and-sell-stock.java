import java.lang.*;

class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        int min_price = Integer.MAX_VALUE;
        for (int price: prices) {
            min_price = Math.min(price, min_price);
            profit = Math.max(profit, price-min_price);
        }
        return profit;
    }
}