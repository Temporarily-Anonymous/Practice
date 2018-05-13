class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        two_time_list = []
        for i in nums:
            if nums[abs(i) - 1] < 0:
                two_time_list.append(abs(i))
            else:
                nums[abs(i) - 1] *= -1
        return two_time_list

Demo = Solution()
result = Demo.findDuplicates([4,3,2,7,7,2,3,1])
print(result)