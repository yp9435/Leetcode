class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Pointers for nums1, nums2, and the merged array
        p1 = m - 1  # Last valid element in nums1
        p2 = n - 1  # Last element in nums2
        p = m + n - 1  # Last position in nums1

        # Merge nums1 and nums2 from the back
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, add them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1