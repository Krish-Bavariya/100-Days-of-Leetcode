# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to store the last seen index of each character
        seen = {}
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            # If the character is already seen and is inside the current window
            if current_char in seen and seen[current_char] >= left:
                # Move the left pointer right past the previous duplicate
                left = seen[current_char] + 1
            
            # Update or insert the character's newest index
            seen[current_char] = right
            
            # Calculate the window size and update max_length if it's larger
            current_window_length = right - left + 1
            max_length = max(max_length, current_window_length)
            
        return max_length