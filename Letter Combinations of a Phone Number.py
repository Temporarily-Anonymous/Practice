class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        number_to_letter_list = {}
        number_to_letter_list['0'] = ['']
        number_to_letter_list['1'] = ['@', '/','.']
        number_to_letter_list['2'] = ['a', 'b', 'c']
        number_to_letter_list['3'] = ['d', 'e', 'f']
        number_to_letter_list['4'] = ['g', 'h', 'i']
        number_to_letter_list['5'] = ['j', 'k', 'l']
        number_to_letter_list['6'] = ['m', 'n', 'o']
        number_to_letter_list['7'] = ['p', 'q', 'r','s']
        number_to_letter_list['8'] = ['t', 'u', 'v']
        number_to_letter_list['9'] = ['w', 'x', 'y','z']
        results = []
        if len(digits) == 0:
            return results
        def find_letter_combinations(digits, str):
            if len(digits) == 0:
                results.append(str)
            else:
                for char in number_to_letter_list[digits[0]]:
                    str += char
                    find_letter_combinations(digits[1:], str)
                    str = str[:-1]
        find_letter_combinations(digits, '')
        return results

Demo = Solution()
result = Demo.letterCombinations("")
print(result)