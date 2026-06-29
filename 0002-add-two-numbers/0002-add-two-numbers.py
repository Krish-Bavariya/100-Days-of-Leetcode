# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # A dummy node acts as the starting anchor for our result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop continues as long as there's a node to process or a leftover carry
        while l1 or l2 or carry:
            # Extract values, defaulting to 0 if a list has run out of nodes
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum for the current position
            total_sum = val1 + val2 + carry
            
            # Update the carry and find the single digit to store
            carry = total_sum // 10
            new_val = total_sum % 10
            
            # Create a new node with the result and move our pointer
            current.next = ListNode(new_val)
            current = current.next
            
            # Advance the input lists pointers if they are not null
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy_head.next