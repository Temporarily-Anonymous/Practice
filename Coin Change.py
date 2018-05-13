import timeit
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        coins.reverse()
        amount_counts = {}
        def find_coin(amount):
            if amount < 0:
                amount_counts[amount] = float('inf')
            elif amount == 0:
                amount_counts[amount] = 0
            elif amount in amount_counts:
                return
            else:
                amount_counts[amount] = float('inf')
                for coin in coins:
                    find_coin(amount - coin)
                    if amount_counts[amount] > amount_counts[amount - coin] + 1:
                        amount_counts[amount] = amount_counts[amount - coin] + 1
        find_coin(amount)
        return -1 if amount_counts[amount] == float('inf') else amount_counts[amount]

    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        result_position = amount
        amount_counts = [float('inf') for i in range(result_position + 1)]
        amount_counts[0] = 0
        for now_amount in range(result_position + 1):
            for coin in range(len(coins)):
                if now_amount - coins[coin] >= 0 and amount_counts[now_amount] > amount_counts[now_amount - coins[coin]] + 1:
                    amount_counts[now_amount] = amount_counts[now_amount - coins[coin]] + 1
        return -1 if amount_counts[result_position] == float('inf') else amount_counts[result_position]


if __name__ == "__main__":
    Demo = Solution()
    result = Demo.coinChange([370,417,408,156,143,434,168,83,177,280,117],9953)
    t = timeit.Timer('Demo.coinChange([370,417,408,156,143,434,168,83,177,280,117],9953)',setup="from __main__ import Demo")
    print(result)
    print(t.timeit(1))
