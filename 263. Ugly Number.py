class Solution:
    def isUgly(self, n: int) -> bool:
        # An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
        if n == 0:
            return False 
        
        while n % 2 == 0:
            n /= 2

        while n % 3 == 0:
            n /= 3

        while n % 5 == 0:
            n /= 5

        return n == 1
