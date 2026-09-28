class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers

        # make a new string but leave only lowercase letters

        new_str = "".join(char.lower() for char in s if char.isalnum())

        # initialise pointers
        l, r = 0, len(new_str) - 1

        # while the pointers haven't met
        while l < r:
            # compare the elements
            if new_str[l] != new_str[r]:
                return False
            elif new_str[l] == new_str[r]:
                l += 1
                r -= 1
        return True