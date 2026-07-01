class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 1. Add (combine) the two arrays
        combined = nums1 + nums2
        
        # 2. Sort the combined array
        combined.sort()
        
        # 3. Find the median
        n = len(combined)
        mid = n // 2
        
        if n % 2 != 0:
            # Odd length: return the middle element
            return float(combined[mid])
        else:
            # Even length: return the average of the two middle elements
            return (combined[mid - 1] + combined[mid]) / 2.0