class Solution {
    private static int[][] DIRECTIONS = {
        {-1, 0}, {1, 0}, {0, -1}, {0, 1}
    };

    public int numIslands(char[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        int ans = 0;

        for (int x=0; x<n; x++) {
            for (int y=0; y<m; y++) {
                if (grid[x][y] == '1') {
                    deleteIslands(x, y, grid);
                    ans++;
                }
            }
        }
        return ans;
    }

    public void deleteIslands(int x, int y, char[][] grid) {
        if (x < 0 || x >= grid.length || y < 0 || y >= grid[0].length)
            return;
        
        if (grid[x][y] != '1') return;

        grid[x][y] = '0';
        
        int nx, ny;
        for (int i=0; i<4; i++) {
            nx = x + DIRECTIONS[i][0];
            ny = y + DIRECTIONS[i][1];

            deleteIslands(nx, ny, grid);
        }
    }
}