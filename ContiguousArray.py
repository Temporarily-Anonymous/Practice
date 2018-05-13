class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums.count(0) == 0 or nums.count(1) == 0:
            return 0
        counter = [0 for i in nums]
        nums_len = len(nums)
        for i in range(nums_len):
            if nums[i] == 1:
                counter[i] = counter[i - 1] + 1
            else:
                counter[i] = counter[i - 1] - 1
        reversed_counter = list(reversed(counter))
        length = 0
        lengths = {}
        for i in range(nums_len):
            if counter[i] == 0:
                length = max(length,nums_len - reversed_counter.index(0))
            try:
                length = max(length, i - lengths[counter[i]])
            except:
                lengths[counter[i]] = i
        return length

Demo = Solution()
result = Demo.findMaxLength([0,0,1,0,0,0,1,1])
print(result)