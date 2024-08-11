import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
  static int N;
  static Set<String> set = new HashSet<String>();
  
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    int T = Integer.parseInt(br.readLine());
    for (int i=1; i<=T; i++) {
      N = Integer.parseInt(br.readLine());
      
      if (N == 0) {
        System.out.println("Case #" + i + ": INSOMNIA");
        continue;
      }
      
      String answer = checkSleep(1);

      System.out.println("Case #" + i + ": " + answer);
      set.clear();
    }
  }

  public static String checkSleep(int cnt) {
    String now = Integer.toString(N);

    while (true) {
      cnt++;

      for (String idx: now.split("")){
        set.add(idx);
      }
      
      if (set.size() == 10) break;
      int temp = cnt * N;
      now = Integer.toString(temp);
    }

    return now;
  }
}
