import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.stream.Stream;

public class Main {
  static int k;
  static int[] numbers;
  static boolean[] visited;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    while(true) {
      String input = br.readLine();
      if (input.equals("0")) return;

      numbers = Stream.of(input.split(" ")).mapToInt(Integer::parseInt).toArray();

      k = numbers[0];
      visited = new boolean[k+1];

      makeLottoSet(1, 0);
      System.out.println("");
    }
  }

  public static void makeLottoSet(int idx, int len) {
    if (len == 6) { //종료 조건
      StringBuilder sb = new StringBuilder("");
      for (int i=1; i<=k; i++) {
        if (visited[i]) {
          sb.append(numbers[i]).append(" ");
        }
      }
      
      System.out.println(sb);
      sb.setLength(0);
      return;
    }

    for (int i=idx; i<=k; i++) {
      if (!visited[i]) {
        visited[i] = true;
        makeLottoSet(i, len+1);
        visited[i] = false;
      }
    }
  }
  
}
