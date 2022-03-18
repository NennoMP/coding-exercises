# https://leetcode.com/problems/climbing-stairs/


class Solution:
    """
        Optimal solution
        - TIME:
        - SPACE:
    """
    
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        x1, x2 = 1, 1
        for i in range(n-1):
            result = x2 + x1
            x1 = x2
            x2 = result
        
        return result
