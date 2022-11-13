class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # rotate 90 deg's is basically transposing the matrix then reversing the rows
    
        
        # transpose matrix
        for row in range(len(matrix)):
            for col in range(row, len(matrix)):
                temp = matrix[row][col]
                matrix[row][col] = matrix[col][row]
                matrix[col][row] = temp
        
        # reverse matrix
        for row in matrix:
            row.reverse()
            
            
        