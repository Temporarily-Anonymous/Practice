class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [0 for i in range(n + 1)]
        result[0] = 1
        for i in range(1,n + 1):
            for j in range(i):
                result[i] += result[i - 1 - j] * result[j]
        return result[n]

Demo = Solution()
result = Demo.numTrees(5)
print(result)