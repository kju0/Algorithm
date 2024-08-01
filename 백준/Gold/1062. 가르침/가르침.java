import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

  static int N, K;
  static int answer = Integer.MIN_VALUE;
  static boolean[] visited;
  static String[] words;

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());
    N = Integer.parseInt(st.nextToken());
    K = Integer.parseInt(st.nextToken());

    // 예외 케이스 정리
    if (K < 5) {
      System.out.println("0");
      return;
    } else if (K == 26) {
      System.out.println(N);
      return;
    }

    words = new String[N];
    for (int i=0; i<N; i++){
      String word = br.readLine();
      word = word.replace("anta", "").replace("tica", "");
      words[i] = word;
    }

    // 방문 처리
    visited = new boolean[26];
    visited['a'-'a'] = true;
    visited['c'-'a'] = true;
    visited['i'-'a'] = true;
    visited['n'-'a'] = true;
    visited['t'-'a'] = true;

    backtracking(0, 0);
    System.out.println(answer);

  }


  // 백트래킹 함수
  public static void backtracking(int alpha, int len) {
    // 종료 조건
    if (len == K-5) {
      int result = 0;
      for (String word: words) {
        boolean check = true;
        for (int l=0; l<word.length(); l++){
          if (!visited[word.charAt(l)-'a']){
            check = false;
            break;
          }
        }

        if (check) result++;
      }

      answer = Math.max(answer, result);
      return;
    }

    // 탐색 조건
    for (int i=alpha; i<26; i++){
      if (!visited[i]) {
        visited[i] = true;
        backtracking(i, len+1);
        visited[i] = false;
      }
    }

  }
}
