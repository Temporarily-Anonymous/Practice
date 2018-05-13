class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                if row == 0 and column == 0:
                    continue
                elif row == 0:
                    grid[row][column] += grid[row][column - 1]
                elif column == 0:
                    grid[row][column] += grid[row - 1][column]
                else:
                    grid[row][column] += min(grid[row][column - 1], grid[row - 1][column])
        return grid[len(grid) - 1][len(grid[0]) - 1]

Demo = Solution()
result = Demo.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
print(result)
