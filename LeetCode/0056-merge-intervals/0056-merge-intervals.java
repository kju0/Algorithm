import java.util.*;

class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, Comparator.comparing((a -> a[0])));
        ArrayList<int[]> new_arr = new ArrayList<>();


        int nowX = intervals[0][0], nowY = intervals[0][1];

        for (int idx=1; idx<intervals.length; ++idx) {
            if (intervals[idx][0] <= nowY) {
                nowY = Math.max(intervals[idx][1], nowY);
            } else {
                new_arr.add(new int[] {nowX, nowY});
                nowX = intervals[idx][0];
                nowY = intervals[idx][1];
            }
        }
        new_arr.add(new int[] {nowX, nowY});

        // 변환 작업
        int [][] answer = new int[new_arr.size()][2];
        for (int i=0; i<new_arr.size(); ++i) {
            answer[i] = new_arr.get(i);
        }
        return answer;
    }
}