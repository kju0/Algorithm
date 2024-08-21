import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    int k = sc.nextInt();
    sc.close();

    long start = 1;
    long end = k;
    long mid = 0;
    while (start < end){
      long cnt = 0;
      mid = (start+end)/2;
      
      for (int i=1; i<=N; i++) {
        cnt += Math.min(mid/i, N);
      }

      if (cnt >= k) {
        end = mid;
      }
      else start = mid+1;
    }

    System.out.println(start);
  }
}
