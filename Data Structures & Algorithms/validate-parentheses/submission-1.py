class Solution:
    def isValid(self, s: str) -> bool:
        # we can use a stack to keep track of the opening brackets

        # create a hash table with the keys as closing brackets, and values as opening brackets
        hash_table = {")": "(", "}": "{", "]": "["}
        # create a stack
        stack = []

        # loop through the brackets in the string
        for b in s:
            # if bracket is in the hash table
            if b in hash_table:
                # if the stack is not empty and the last element of the stack matches the closing bracket in the hash table
                # ie we found the closing bracket
                if stack and stack[-1] == hash_table[b]:
                    # remove the opening bracket from the top of the stack
                    stack.pop()
                else:
                    return False
            # otherwise the bracket is not in the hash table so push the opening bracket to the stack
            else:
                stack.append(b)
        # only return True if the stack is empty (it means all brackets have been matched
        return True if not stack else False
