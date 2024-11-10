def solution(board):
    def insert_danger(x, y):
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 > nx) or (nx >= n) or (0 > ny) or (ny >= n):
                continue
            
            danger.add((nx, ny))
        
    n = len(board)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1] #상하좌우
    dy = [0, 0, -1, 1, -1, 1, -1, 1] #상하좌우
    
    answer = 0
    
    danger = set()
    for x in range(n):
        for y in range(n):
            if board[x][y] == 1:
                insert_danger(x, y)
                danger.add((x, y))
    
    #print(set(danger))
    return n*n - len(set(danger))