class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def check(start, target):
            if start[0] < target[0] and start[1] < target[1]:
                return 1
            if start[0] < target[0] and start[1] > target[1]:
                return 2
            if start[0] > target[0] and start[1] > target[1]:
                return 3
            if start[0] > target[0] and start[1] < target[1]:
                return 4
        

        answer = 0
        chk_result = [0, 0]
        check_result = [[0,0], [1, 1], [1, -1], [-1, -1], [-1, 1]]
        n = len(points)

        for i in range(n):
            if i == n-1:
                return answer
            
            start = [points[i][0], points[i][1]]
            target = [points[i+1][0], points[i+1][1]]

            while (start[0]!=target[0] and start[1]!=target[1]):
                chk_result = check_result[check(start, target)]
                start[0] += chk_result[0]
                start[1] += chk_result[1]
                answer += 1

            if start[0] == target[0] and start[1] != target[1]:
                answer += abs(target[1] - start[1])
            elif start[0] != target[0] and start[1] == target[1]:
                answer += abs(target[0] - start[0])

        return answer