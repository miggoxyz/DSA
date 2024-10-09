class Solution:
    def calculateFactorial(self, n):
        if n < 0:
            raise RecursionError("Negative number")
        if n == 0 or n == 1:
            return 1
        return n * self.calculateFactorial(n-1)
