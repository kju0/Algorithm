import java.util.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) return 0;

        Set<Character> check_now = new HashSet<>();
        int max_len = 0;
        int idx = 0;
        int prev = 0;
        
        while (idx < s.length()) {
            if (!check_now.contains(s.charAt(idx))) {
                check_now.add(s.charAt(idx));
                idx++;
            } else {
                max_len = Math.max(max_len, check_now.size());
                check_now.remove(s.charAt(prev));
                prev++;
            }
        }
        max_len = Math.max(max_len, check_now.size());
        return max_len;
    }
    
}

