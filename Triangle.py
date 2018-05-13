class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j] = triangle[i][j] + triangle[i - 1][j]
                elif j == len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i][j] + triangle[i - 1][j - 1]
                else:
                    triangle[i][j] = min(triangle[i][j] + triangle[i - 1][j], triangle[i][j] + triangle[i - 1][j - 1])
        return min(triangle[-1])

a = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
Demo = Solution()
result = Demo.minimumTotal(a)
print(result)