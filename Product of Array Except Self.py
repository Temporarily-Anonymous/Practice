class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums.count(0) > 1:
            return [0]*len(nums)
        product_of_all = 1
        results = []
        for i in nums:
            if i is not 0:
                product_of_all *= i
        if nums.count(0) == 1:
            zero_position = nums.index(0)
            return [0]*zero_position + [product_of_all] + [0]*(len(nums) - zero_position - 1)
        for i in nums:
            results.append(int(product_of_all/i))
        return results

Demo = Solution()
result = Demo.productExceptSelf([1,2,0,3,4])
print(result)

