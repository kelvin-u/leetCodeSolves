class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # tranpose the matrix then reverse the rows
        
        # tranpose matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        #reverse matrix 
        for i in matrix:
            i.reverse()
            
            
            
        