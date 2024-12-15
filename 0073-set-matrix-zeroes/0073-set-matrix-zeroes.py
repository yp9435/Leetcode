class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False #extra variable to make up for the missing space.

        # matrix[0][c] and matrix[r][0]

        #mark the first row and first col if there any zeros
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0

                    if r>0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True
        
        #now based on the first row and col, mark the remaining elements zero
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        #mark first row zero
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        #mark first col zero
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0