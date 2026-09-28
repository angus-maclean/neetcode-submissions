class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # initialise the pointers at the start and end
        i, j = 0, len(numbers)-1

        # while the pointers are valid
        while i < j:
            # sum the values at the indexes i and j
            s = numbers[i] + numbers[j]
            # if the sum equals the target
            if s == target:
                # return a list with the indexes
                return [i+1,j+1]
            elif s < target:
                i += 1
            elif s > target:
                j -= 1
        return None