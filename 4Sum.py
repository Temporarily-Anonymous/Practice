class Solution:

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        nums_len = len(nums)
        for i in range(nums_len - 3):
            if target - nums[i] <= sum(nums[-3:]) and target - nums[i] >= sum(nums[i+1:i+4]):
                for j in range(i + 1, nums_len - 2):
                    if target - nums[i] - nums[j] <= sum(nums[-2:]) and target - nums[i] - nums[j] >= sum(nums[j+1:j+3]):
                        for k in range(j + 1, nums_len - 1):
                            num4 = target - nums[i] - nums[j] - nums[k]
                            if num4 in nums[k+1:]:
                                new_result = [nums[i], nums[j], nums[k], num4]
                                new_result.sort()
                                if new_result not in result:
                                    result.append(new_result)
        print(result)

Demo = Solution()
nums = [1,-2,-5,-4,-3,3,3,5]
target = -11
result = Demo.fourSum(nums, target)