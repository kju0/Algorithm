class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        answer = 0

        countList = [[0 for i in range(m)], [0 for j in range(n)]]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    countList[0][i] += 1
                    countList[1][j] += 1
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if countList[0][i] == 1 and countList[1][j] == 1:
                        answer += 1
        
        return answer