class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> answerList = new ArrayList<>(); //그 자체로 업캐스팅
        backtrace(answerList, "", 0, 0, n);

        return answerList;
    }

    public void backtrace(List<String> answerList, String res, int open, int close, int n) {
        if (res.length() == n*2) answerList.add(res);
        if (open < n) {
            //res = (new StringBuilder()).append(res).append("(").toString();
            backtrace(answerList, res + "(", open+1, close, n);
        }
        if (close < open) {
            //res = (new StringBuilder()).append(res).append(")").toString();
            backtrace(answerList, res + ")", open, close+1, n);
        }
    }
}
    