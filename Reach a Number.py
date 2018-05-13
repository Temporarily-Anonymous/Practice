import math
import queue
class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        step = 0
        position = 0
        while position < target:
            step += 1
            position += step
        if position == target:
            return step
        else:
            remainder_step = position - target
            return step if remainder_step%2 == 0 else step + step % 2 + 1

Demo = Solution()
result = Demo.reachNumber(10000000)
print(result)