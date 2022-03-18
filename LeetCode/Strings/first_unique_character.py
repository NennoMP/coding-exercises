# Amazon Coding Assessments Part 1: 26-11-2021


"""
Given a string of only lower case english letters
:return: 
    - index of the first unique character, if it exists
    - -1, if it does not exist
"""
class Solution:
    """
    Optimal solution
    - TIME:
    - SPACE:
    """

    def isUnique(self, s: str) -> int:
        hashmap: dict = {}

        for c in s:
            if c not in hashmap:
                hashmap[c] = 1
            else:
                hashmap[c] += 1

        for i, c in enumerate(s):
            if hashmap[c] == 1:
                return i
        
        return -1