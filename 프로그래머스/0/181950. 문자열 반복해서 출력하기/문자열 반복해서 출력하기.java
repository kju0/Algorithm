import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int n = sc.nextInt();
        
        List<String> answers = new ArrayList<>();
        
        for (int i=0; i<n; i++) {
            answers.add(str);
        }
        
        for (String answer : answers) {
            System.out.print(answer);
        }
    }
}