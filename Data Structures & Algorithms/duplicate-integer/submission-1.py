class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we are returning True if there is a duplicate
        # we can use a seen dictionary

        seen = {}

        for num in nums:
            if num in seen:
                return True
            seen[num] = 0
        return False
