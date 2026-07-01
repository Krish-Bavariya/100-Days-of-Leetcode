class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
            
        longest = ""
        
        for i in range(len(s)):
            # Check for Odd palindromes (e.g., "aba", center is 'b')
            # Check for Even palindromes (e.g., "abba", center is between 'b' and 'b')
            for left, right in ((i, i), (i, i + 1)):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
                
                # After the while loop breaks, s[left+1 : right] is the valid palindrome
                current_palindrome = s[left + 1:right]
                if len(current_palindrome) > len(longest):
                    longest = current_palindrome
                    
        return longest