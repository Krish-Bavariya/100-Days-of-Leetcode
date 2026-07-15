# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the width between the two pointers
            width = right - left
            
            # The water level is limited by the shorter line
            current_height = min(height[left], height[right])
            
            # Calculate the area and update max_water if this is larger
            current_area = width * current_height
            max_water = max(max_water, current_area)
            
            # Move the pointer that points to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water