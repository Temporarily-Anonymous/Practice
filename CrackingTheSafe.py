class Solution():
    def FindMinString(self, last_str, undisposed, k):
        if not undisposed:
            return last_str
        else:
            common_str = last_str[1:]
            for new_portion in range(k):
                new_str = common_str + str(new_portion)
                if new_str in undisposed:
                    undisposed.remove(new_str)
                    try:
                        return last_str[0] + self.FindMinString(new_str, undisposed, k)
                    except:
                        undisposed.append(new_str)

    def crackSafe(self, n, k):
        sum = k ** n
        undisposed = []
        number_str = ""
        for number in range(sum):
            for i in range(n):
                temp = number % k
                number_str = str(temp) + number_str
                number = int((number - temp) / k)
            undisposed.append(number_str)
            number_str = ""
        start = undisposed[0]
        undisposed.remove(undisposed[0])
        return self.FindMinString(start, undisposed, k)

Demo = Solution()
result = Demo.crackSafe(2, 2)