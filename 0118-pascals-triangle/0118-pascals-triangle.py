class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(1,numRows+1):
            row = [1]
            ans = 1
            for col in range(1, i):
                ans *= (i - col)
                ans //= col
                row.append(ans)
            triangle.append(row)
        return triangle