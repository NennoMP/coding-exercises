# https://leetcode.com/problems/two-sum/


class Solution(object):
    """
        Optimal Solution
        - TIME:
        - SPACE:
    """
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap: dict = {}
            
        for i, v in enumerate(nums):
            complement = target - v
            if complement in hashmap:
                return [i, hashmap[complement]]

            hashmap[v] = i
