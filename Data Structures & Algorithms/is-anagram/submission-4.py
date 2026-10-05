class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we need to count each letter


        # map the letter to the count so char:count
        t_count = {}
        s_count = {}

        for char in t:
            if char in t_count:
                t_count[char] += 1
            else: 
                t_count[char] = 1
        
        for char in s:
            if char in s_count:
                s_count[char] += 1
            else: 
                s_count[char] = 1

        if t_count == s_count:
            return True
        return False


        