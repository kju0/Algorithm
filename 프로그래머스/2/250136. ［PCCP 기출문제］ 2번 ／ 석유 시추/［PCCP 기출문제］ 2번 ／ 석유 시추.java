import java.util.*;
class Solution {
    
    private static int N, M;
    private static int[][] moves = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    private static List<int[]> block;
    private static List<List<int[]>> blocks = new ArrayList<>();
    private static boolean visited[][];
    private static Map<Integer, Integer> columnBlockCount = new HashMap<>();
    private static int answer = 0;
    
    
    public int solution(int[][] land) {
        N = land.length; //행
        M = land[0].length; //열
        
        visited = new boolean[N][M];
        
        // 블록 수 구하기
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (land[i][j] == 1 && visited[i][j] == false) {
                    block = new ArrayList<>();
                    dfs(i, j, land);
                    blocks.add(block);
                    
                    boolean [] pos_visited = new boolean[M];
                    // 블록이 포함된 열에 대한 정보 기록
                    for (int[] pos : block) {
                        
                        int col = pos[1];
                        if (pos_visited[col] == false) {
                            columnBlockCount.put(col, columnBlockCount.getOrDefault(col, 0) + block.size());
                            pos_visited[col] = true;
                        }
                            
                    }
                }
            }
        }
        
        // 최대 석유 시추 수
        for (int col = 0; col < M; col++) {
            answer = Math.max(answer, columnBlockCount.getOrDefault(col, 0));
        }
        
        return answer;
    }
    
    private static void dfs(int x, int y, int[][] land) {
        visited[x][y] = true;
        block.add(new int[] {x, y});
        
        int nx, ny;
        for (int[] move: moves){
            nx = x + move[0];
            ny = y + move[1];
            
            if (0 > nx || nx >= N || 0 > ny || ny >= M) continue;
            
            if (land[nx][ny] == 1 && visited[nx][ny] == false) dfs(nx, ny, land);
        }
    }
}