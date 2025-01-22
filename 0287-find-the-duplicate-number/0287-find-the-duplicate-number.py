class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initial slow and fast pointers
        slow, fast = 0, 0

        # Phase 1: Detect the cycle
        while True:
            slow = nums[slow]  # Move slow one step
            fast = nums[nums[fast]]  # Move fast two steps
            if slow == fast:  # Cycle detected
                break

        # Phase 2: Find the start of the cycle (duplicate)
        slow2 = 0  # Initialize second slow pointer
        while True:
            slow = nums[slow]  # Move slow one step
            slow2 = nums[slow2]  # Move slow2 one step
            if slow == slow2:  # Both pointers meet at the duplicate
                return slow
