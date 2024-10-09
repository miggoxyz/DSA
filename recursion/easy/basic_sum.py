"""
Time:   O(n) because we make N recursive calls, 
        where N is the input of natural numbers
Space:  O(n) because the max depth of the recursion is N
        each recursive call adds a new stack frame,
        consuming additional space on the call stack
"""


class Solution:
    def calculateSum(self, n):
        if n <= 0:
            return 0
        return n + self.calculateSum(n-1)
