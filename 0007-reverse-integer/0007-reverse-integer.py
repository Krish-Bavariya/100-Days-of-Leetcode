# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define 32-bit signed integer boundaries
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Determine the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        reversed_num = 0
        while x != 0:
            # Pop the last digit
            digit = x % 10
            x //= 10
            
            # Push the digit onto the reversed number
            reversed_num = (reversed_num * 10) + digit
            
        # Reapply the sign
        reversed_num *= sign
        
        # Check for 32-bit overflow
        if reversed_num < INT_MIN or reversed_num > INT_MAX:
            return 0
            
        return reversed_num