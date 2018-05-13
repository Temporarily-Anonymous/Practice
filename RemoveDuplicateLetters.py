class Solution:
    def removeDuplicateLetters(self, s):
        char_list = sorted(set(s))
        for char in char_list:
            position = s.index(char)
            next_string = s[position:]
            if set(next_string) == set(s):
                return char + self.removeDuplicateLetters(next_string.replace(char,''))
        return ''

Demo = Solution()
result = Demo.removeDuplicateLetters("cbacdcbc")
print(result)
