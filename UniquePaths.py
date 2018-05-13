class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        paths = [[1 for i in range(n)] for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                paths[i][j] = paths[i][j-1] + paths[i-1][j]
        return paths[m-1][n-1]


Demo = Solution()
Demo.uniquePaths(3, 7)