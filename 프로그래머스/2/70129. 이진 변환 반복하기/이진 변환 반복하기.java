class Solution {
    private static int changeCnt = 0;
    private static int removeCnt = 0;
    
    public int[] solution(String s) {
        int[] answer = new int [2];
        
        
        binary(s);
        
        answer[0] = changeCnt;
        answer[1] = removeCnt;
        
        return answer;
    }
    
    private static void binary(String s) {
        if (s.equals("1")) return;
        
        String temp = s.replace("0", "");
        removeCnt += s.length() - temp.length();
        changeCnt++;
        
        int size = temp.length();
        binary(Integer.toBinaryString(size));
    }
}