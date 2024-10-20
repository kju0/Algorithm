import java.util.*;
class Node implements Comparable<Node>{
    int idx;
    int cost;

    public Node(int idx, int cost) {
        this.idx = idx;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        return Integer.compare(this.cost, o.cost);
    }
}

class Solution {
    static List<Node>[] graph;
    

    public int solution(int n, int s, int a, int b, int[][] fares) {
        graph = new ArrayList[n+1];
        int answer = Integer.MAX_VALUE;
        
        for (int i=0; i<= n; i++) graph[i] = new ArrayList<>();
        
        for (int [] fare : fares) {
            graph[fare[0]].add(new Node(fare[1], fare[2]));
            graph[fare[1]].add(new Node(fare[0], fare[2]));
        }
        
        int[] commonDist = Dijkstra(n, s);
        
        /*for (int val : commonDist) {
            System.out.println(val);
        }*/
        
        for (int i=1; i<=n; i++) {
            int temp = commonDist[i];
            
            temp += Dijkstra_target(n, i, a) + Dijkstra_target(n, i, b);
            
            answer = Math.min(answer, temp);
        }
        
        
        return answer;
    }
    
    private static int[] Dijkstra(int n, int start) {
        boolean[] visited = new boolean[n+1];
        int[] dist = new int[n+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;
        
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));
        
        while (!pq.isEmpty()){
            int nowIdx = pq.poll().idx;
            
            if (visited[nowIdx]) continue;
            visited[nowIdx] = true;
            
            for (Node next : graph[nowIdx]) {
                if (dist[next.idx] > dist[nowIdx] + next.cost) {
                    dist[next.idx] = dist[nowIdx] + next.cost;
                    pq.offer(new Node(next.idx, dist[next.idx]));
                }
            }
        }
        
        return dist;
    }
    
        private static int Dijkstra_target(int n, int start, int target) {
        boolean[] visited = new boolean[n+1];
        int[] dist = new int[n+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;
        
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));
        
        while (!pq.isEmpty()){
            int nowIdx = pq.poll().idx;
            
            if (visited[nowIdx]) continue;
            visited[nowIdx] = true;
            
            if (nowIdx == target) return dist[target];
            
            for (Node next : graph[nowIdx]) {
                if (dist[next.idx] > dist[nowIdx] + next.cost) {
                    dist[next.idx] = dist[nowIdx] + next.cost;
                    pq.offer(new Node(next.idx, dist[next.idx]));
                }
            }
        }
        
        return dist[target];
    }
}