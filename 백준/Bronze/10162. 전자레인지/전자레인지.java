import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int time = sc.nextInt();
    sc.close();

    if (time % 10 != 0) {
      System.out.println(-1);
      return;
    }
    int aCnt = 0;
    int bCnt = 0;
    int cCnt = 0;

    if (time >= 300) {
      aCnt = time / 300;
      time -= aCnt*300;
    }

    if (time >= 60) {
      bCnt = time / 60;
      time -= bCnt*60;
    }

    if (time >= 10) {
      cCnt = time / 10;
      time -= cCnt*60;
    }

    System.out.println(aCnt+" "+bCnt+" "+cCnt);

  }
  
}
