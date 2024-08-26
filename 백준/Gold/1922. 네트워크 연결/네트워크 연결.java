import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
  static int N;
  static int M;
  // 크루스칼 알고리즘 union by rank + 우선순위큐 edges
  // 사이클 확인을 위한 union by rank
  static int[] parent;
  static int[] rank;

  static int find(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find(parent[x]);
  }

  static void union(int x, int y) {
    x = find(x);
    y = find(y);

    if (x==y) return;

    if (rank[x] < rank[y]) {
      parent[x] = y;
    } else {
      parent[y] = x;

      if (rank[x] == rank[y]) rank[x]++;
    }
  }

  // cost 순서로 정렬할 수 있는 우선순위큐 Edge
  static PriorityQueue<Edge> edges;

  static class Edge implements Comparable<Edge> {
    int from;
    int to;
    int cost;

    public Edge(int from, int to, int cost){
      this.from = from;
      this.to = to;
      this.cost = cost;
    }

    @Override
    public int compareTo(Edge o){
      return this.cost - o.cost;
    }
  }
  public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    N = Integer.parseInt(br.readLine());
    M = Integer.parseInt(br.readLine());

    parent = new int[N+1];
    rank = new int[N+1];

    edges = new PriorityQueue<>();

    for (int i=1; i<=N; i++) {
      parent[i] = i;
    }

    for (int i=0; i<M; i++){
      StringTokenizer st = new StringTokenizer(br.readLine());
      int from = Integer.parseInt(st.nextToken());
      int to = Integer.parseInt(st.nextToken());
      int cost = Integer.parseInt(st.nextToken());

      edges.add(new Edge(from, to, cost)); // 우선순위 큐 넣으면서 정렬!
    }

    int answer = 0;

    while (!edges.isEmpty()){
      Edge edge = edges.poll();

      if (find(edge.from) == find(edge.to)) continue;

      union(edge.from, edge.to);
      answer += edge.cost;
    }

    System.out.println(answer);
  }
}
