class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        char_list = list(set(S))
        char_number = {}
        for c in char_list:
            char_number[c] = S.count(c)
        num, char = max(zip(char_number.values(), char_number.keys()))
        if (len(S)%2 == 0 and num > len(S)/2) or (len(S)%2 == 1 and num >len(S)/2 +1):
            return ""
        else:
            result = char
            for i in range(len(S) - 1):
                last_num = num
                last_char =char
                char_number[last_char] = 0
                num, char = max(zip(char_number.values(),char_number.keys()))
                result += char
                char_number[last_char] = last_num - 1
            return result
Demo = Solution()
result = Demo.reorganizeString("aaab")