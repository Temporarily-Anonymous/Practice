class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        result = [False for i in range(len(s) + 1)]
        result[0] = True
        cut_off_point = {}
        for i in range(1, len(s) + 1):
            position = 0
            cut_off_point[i] = []
            while True:
                if s[position:i] in wordDict:
                    result[i] = True
                    if position is not 0:
                        cut_off_point[i].append(position)
                if True in result[position + 1:i]:
                    position = result[:i].index(1, position + 1)
                else:
                    break
        sentence = []
        def wordBreak(s, point):
            if cut_off_point[point] == []:
                sentence.append(s)
            else:
                for i in cut_off_point[point]:
                    wordBreak(s[:i] + ' ' + s[i:], i)
        print(cut_off_point)
        if result[len(s)] is False:
            return []
        else:
            wordBreak(s, len(s))
            print(len(sentence))
            return sentence


s = "aaaaaaa"
dict = ["aaaa","aa","a"]
Demo = Solution()
result = Demo.wordBreak(s, dict)
print(result)
