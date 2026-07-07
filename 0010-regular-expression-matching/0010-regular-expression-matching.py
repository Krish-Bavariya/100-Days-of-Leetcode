# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        
        # Initialize a DP table of size (m+1) x (n+1) with False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty string matches empty pattern
        dp[0][0] = True
        
        # Base case: handle patterns that can match an empty string (e.g., "a*", "a*b*")
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
                
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Case 1: The current pattern character is a text char or '.'
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                    
                # Case 2: The current pattern character is '*'
                elif p[j - 1] == '*':
                    # Subcase 2a: Count '*' and its preceding element as 0 occurrences
                    dp[i][j] = dp[i][j - 2]
                    
                    # Subcase 2b: Count '*' as 1 or more occurrences
                    # (Only valid if the preceding character in p matches the current character in s)
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                        
        return dp[m][n]