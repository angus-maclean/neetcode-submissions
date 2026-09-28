class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # list is unsorted so we can't use two pointers unless we sort it first, but then can't use the ORIGINAL indices per the question
    # if we did then we could be iterating many times through the list

        # so because it is unsorted we need a dictionary
        seen = {}
        
        # use enumerate to get the index of each num in the array
        for i, num in enumerate(nums):
            # specify the complement
            difference = target - num
            # check if the difference is in the dictionary
            if difference in seen:
                # return the indices of the difference and the index of the current num
                return [seen[difference], i]
            # if not then add the current num to the seen dictionary and map to its index
            seen[num] = i

