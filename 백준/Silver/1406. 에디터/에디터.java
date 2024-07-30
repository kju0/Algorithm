import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringBuilder sb = new StringBuilder();
    sb.append(br.readLine());
    
    int cursor = sb.length();

    int n = Integer.parseInt(br.readLine());

    StringTokenizer st;
    for (int i=0; i<n; i++) {
      st = new StringTokenizer(br.readLine());

      String now = st.nextToken();
      if (now.equals("L")) {
        cursor = ((cursor-1) < 0) ? cursor : cursor-1;
      } else if (now.equals("D")) {
        cursor = ((cursor+1) > sb.length()) ? cursor : cursor+1;
      } else if (now.equals("B")) {
        if (cursor == 0) continue;
        sb.deleteCharAt(cursor-1);
        cursor--;
      } else if (now.equals("P")){
        sb.insert(cursor, st.nextToken());
        cursor++;
      }
    }

    System.out.println(sb);
    
  }
}
