class Solution
{
    public int solution(int n, int a, int b)
    {
        int newA, newB;
        
        int answer = 0;
        while (true) {
            //A와 B가 같은 대진표를 얻게 될 때
            newA = calculate(a);
            newB = calculate(b);
            
            if (newA == newB) break;
            
            a = newA;
            b = newB;
            
            answer++;
            
        }

        return answer+1;
    }
    
    private static int calculate(int n) {
        int target;
        if (n%2 == 0) {
            target = n/2;
        } else {
            target = n/2 + 1;
        }
        return target;
    }
}