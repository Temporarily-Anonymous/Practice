class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0
        wide = len(obstacleGrid)
        length = len(obstacleGrid[0])
        for i in range(wide):
            for j in range(length):
                if i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                elif j == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[wide - 1][length - 1]


a = [[0]]
Demo = Solution()
result = Demo.uniquePathsWithObstacles(a)
print(result)