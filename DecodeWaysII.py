class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] is "0":
            return 0
        result = {}
        mod = pow(10,9) + 7
        result[-1] = 1
        result[0] = 1 if s[0] is not "*" else 9
        length = len(s)
        last_char = s[0]
        i = 1
        while i < length:
            if s[i] is "0":
                if last_char is "1" or last_char is "2" :
                    result[i] = result[i - 2]
                elif last_char is "*":
                    result[i] = 2 * result[i - 2]
                else:
                    return 0
            elif s[i] is "*":
                if last_char is "1":
                    result[i] = 9 * result[i - 2] + 9 * result[i - 1]
                elif last_char is "2":
                    result[i] = 6 * result[i - 2] + 9 * result[i - 1]
                elif last_char is "*":
                    result[i] = 15 * result[i - 2] + 9 * result[i - 1]
                else:
                    result[i] = 9 * result[i - 1]
            else:
                if last_char is "*":
                    if s[i] > "6" :
                        result[i] = result[i - 2] + result[i - 1]
                    else:
                        result[i] = 2 * result[i - 2] + result[i - 1]
                elif int(s[i-1:i+1]) > 26 or last_char is "0":
                    result[i] = result[i - 1]
                else:
                    result[i] = result[i - 2] + result[i - 1]
            last_char = s[i]
            i += 1
            del result[i - 3]
        return result[length - 1] % mod

Demo = Solution()
result = Demo.numDecodings("*********")
print(result)