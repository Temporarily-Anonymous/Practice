class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 1:
            return nums[0]
        mid = int(length/2)
        mid_max_left = float("-inf")
        mid_max_right = float("-inf")
        temp = 0
        for i in range(mid - 1, -1, -1):
            temp += nums[i]
            if temp > mid_max_left:
                mid_max_left = temp
        temp = 0
        for i in range(mid, length):
            temp += nums[i]
            if temp > mid_max_right:
                mid_max_right = temp
        return max(self.maxSubArray(nums[:mid]), self.maxSubArray(nums[mid:]), mid_max_left + mid_max_right)

Demo = Solution()
result = Demo.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(result)