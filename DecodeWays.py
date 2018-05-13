# 动态规划
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] is "0":
            return 0
        result = {}
        result[-1] = 1
        result[0] = 1
        length = len(s)
        i = 1
        while i < length:
            if s[i] is "0":
                if int(s[i-1:i+1]) > 26 or s[i-1] is "0":
                    return 0
                else:
                    result[i] = result[i - 2]
            else:
                if int(s[i-1:i+1]) > 26 or s[i-1] is "0":
                    result[i] = result[i - 1]
                else:
                    result[i] = result[i - 2] + result[i - 1]
            i += 1
        return result[length - 1]


Demo = Solution()
result = Demo.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")
print(result)