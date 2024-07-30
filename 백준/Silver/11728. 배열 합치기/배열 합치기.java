import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());
    int lenA = Integer.parseInt(st.nextToken());
    int lenB = Integer.parseInt(st.nextToken());

    ArrayList<Integer> arrayA = new ArrayList<>();
    ArrayList<Integer> arrayB = new ArrayList<>();

    st = new StringTokenizer(br.readLine());
    while (st.hasMoreTokens()) {
      arrayA.add(Integer.parseInt(st.nextToken()));
    }

    st = new StringTokenizer(br.readLine());
    while (st.hasMoreTokens()) {
      arrayB.add(Integer.parseInt(st.nextToken()));
    }

    int idxA = 0;
    int idxB = 0;

    StringBuilder sb = new StringBuilder();

    while (idxA < lenA && idxB < lenB) {
      if (arrayA.get(idxA) <= arrayB.get(idxB)) {
        sb.append(arrayA.get(idxA)).append(" ");
        idxA++;
      } else {
        sb.append(arrayB.get(idxB)).append(" ");
        idxB++;
      }
    }

    // 남아 있는 원소들 추가
    while (idxA < lenA) {
      sb.append(arrayA.get(idxA)).append(" ");
      idxA++;
    }

    while (idxB < lenB) {
      sb.append(arrayB.get(idxB)).append(" ");
      idxB++;
    }

    // 최종 결과 출력
    System.out.println(sb.toString());
  }
}
