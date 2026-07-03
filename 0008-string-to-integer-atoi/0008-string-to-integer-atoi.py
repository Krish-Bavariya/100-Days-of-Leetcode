# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Define 32-bit signed integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        n = len(s)
        i = 0
        
        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
            
        # If the string is empty or only contained spaces
        if i == n:
            return 0
            
        # Step 2: Check for sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # Step 3: Convert digits
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = (result * 10) + digit
            i += 1
            
        # Apply the sign
        result *= sign
        
        # Step 4: Round/Clamp to 32-bit signed integer boundaries
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
            
        return result