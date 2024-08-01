import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  static int N;
  static boolean visited[];
  static StringBuilder answer;
  
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    N = Integer.parseInt(br.readLine());

    visited = new boolean[N + 1];
    answer = new StringBuilder();

    backtracking(0);
  }

  private static void backtracking(int len) {
    if (len == N) {
      System.out.println(answer.toString().trim());
      return;
    }

    for (int i = 1; i <= N; i++) {
      if (!visited[i]) {
        visited[i] = true;
        answer.append(i).append(" ");
        backtracking(len + 1);
        answer.setLength(answer.length() - 2); // 이전 상태로 되돌림
        visited[i] = false;
      }
    }
  }
}
