class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        break_pt = -1

        # 1. Find the break point from the end where nums[i] < nums[i+1]
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break_pt = i
                break

        # 2. If no break point exists, reverse the entire array (last permutation case)
        if break_pt == -1:
            nums.reverse()
            return

        # 3. Find the first element larger than nums[break_pt] from the end
        for i in range(n - 1, break_pt, -1):
            if nums[i] > nums[break_pt]:
                # Swap elements at break_pt and i
                nums[i], nums[break_pt] = nums[break_pt], nums[i]
                break

        # 4. Reverse the part of the array after break_pt
        nums[break_pt + 1:] = reversed(nums[break_pt + 1:])

        