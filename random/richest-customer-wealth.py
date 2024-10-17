class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        actual = 0
        for account in accounts:
            wealth = sum(account)
            wealth = max(wealth, actual)
            actual = wealth
        return wealth
        # actual = 0
        # wealth = 0
        # for account in accounts:
        #     for acc in account:
        #         actual = actual + acc
        #     if (actual >= wealth):
        #         wealth = actual
        #     actual = 0
        # return wealth
# https://leetcode.com/problems/richest-customer-wealth/description/