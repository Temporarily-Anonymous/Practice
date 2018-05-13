class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        result = [False for i in range(len(s) + 1)]
        result[0] = True
        for i in range(1, len(s) + 1):
            position = 0
            while True:
                if s[position:i] in wordDict:
                    result[i] = True
                if True in result[position + 1:i]:
                    position = result[:i].index(1, position + 1)
                else:
                    break
        return result[len(s)]

s = "aaaaaaa"
dict = ["aaaa","aa","a"]
Demo = Solution()
result = Demo.wordBreak(s, dict)
print(result)