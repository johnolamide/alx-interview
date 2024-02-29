#!/usr/bin/python3
""" This script contains the function definition for makeChange()
"""


def makeChange(coins, total):
    """ determines the fewest number of coins needed to meet a given amount
        total.
        Args:
            coins: amount of coins
            total: total amount
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
