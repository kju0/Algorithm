class Solution {
    public String longestCommonPrefix(String[] strs) {
        // 배열이 빈 경우 공통 접두사는 빈 문자열
        if (strs == null || strs.length == 0) {
            return "";
        }

        String answer = strs[0];

        for (int i = 1; i < strs.length; i++) {
            int max_len = Math.min(answer.length(), strs[i].length());

            int j;
            for (j = 0; j < max_len; j++) {
                if (answer.charAt(j) != strs[i].charAt(j)) {
                    break;
                }
            }

            answer = answer.substring(0, j);

            // 만약 공통 접두사가 빈 문자열이 되면, 더 이상 비교할 필요가 없음
            if (answer.isEmpty()) {
                return "";
            }
        }
        return answer;
    }
}