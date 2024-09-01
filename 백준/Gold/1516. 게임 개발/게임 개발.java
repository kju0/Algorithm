import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());

    int[] cost = new int[N + 1];
    List<List<Integer>> graph = new ArrayList<>();
    int[] entry = new int[N + 1];
    int[] min_cost = new int[N + 1];
    Queue<Integer> queue = new LinkedList<>();

    for (int i = 0; i <= N; i++) {
      graph.add(new ArrayList<>());
    }

    for (int i = 1; i <= N; i++) {
      StringTokenizer st = new StringTokenizer(br.readLine());

      cost[i] = Integer.parseInt(st.nextToken());
      min_cost[i] = cost[i];

      while (true) {
        int temp = Integer.parseInt(st.nextToken()) - 1;
        if (temp == -2) break;

        graph.get(temp + 1).add(i);
        entry[i] += 1;
      }

      if (entry[i] == 0) queue.offer(i);
    }

    while (!queue.isEmpty()) {
      int target = queue.poll();

      for (int i : graph.get(target)) {
        entry[i] -= 1;
        min_cost[i] = Math.max(min_cost[i], min_cost[target] + cost[i]);

        if (entry[i] == 0) queue.offer(i);
      }
    }

    for (int i = 1; i <= N; i++) {
      System.out.println(min_cost[i]);
    }
  }
}
