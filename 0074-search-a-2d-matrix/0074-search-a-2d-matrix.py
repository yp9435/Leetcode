class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Binary search to find the potential row where the target might exist
        low, high = 0, ROWS - 1
        while low <= high:
            midrow = low + ((high - low) // 2)

            # If the target is smaller than the first element of the middle row,
            # search in the rows above (move high pointer)
            if target < matrix[midrow][0]:
                high = midrow - 1
            
            # If the target is greater than the last element of the middle row,
            # search in the rows below (move low pointer)
            elif target > matrix[midrow][-1]:
                low = midrow + 1
            
            # If the target is within the range of the current row, stop the loop
            else:
                break

        # If no valid row is found (low pointer exceeds high pointer), return False
        if not (low <= high):
            return False
        
        # get the target row where the loop broke off 
        targetrow = low + ((high - low) // 2)

        # normal binary search in target row.
        L, R = 0, COLS - 1
        while L <= R:
            M = L + ((R - L) // 2)
            if matrix[targetrow][M] == target:
                return True
            elif target < matrix[targetrow][M]:
                R = M - 1
            else:
                L = M + 1
        return False
