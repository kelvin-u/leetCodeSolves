class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # store the result 
        result = []
        left, right = 0, len(matrix[0])  #2d array so len(matrix[0]) will be 3 you would normally subtract 1 but since it's out its g
        top, bottom = 0, len(matrix)
        
        while left < right and top < bottom:
            # left to right, get every i in the top row
            for i in range(left, right): # set right out of bounds since range is not inclusive but we want it to go outta bounds
                                         # in order to change direction
                result.append(matrix[top][i])
            top += 1
            # top to bottom, get every i in the right col
            for i in range(top, bottom):
                result.append(matrix[i][right-1])
            right -= 1
            
            if not (left < right and top < bottom):
                break
            # [1,2,3] check this for
            
            # right to left, get every i in the bottom row
            for i in range(right-1, left-1, -1): # -1 since you're going backwards
                result.append(matrix[bottom-1][i])
            bottom -= 1
            
            # bottom to top, get every in the left col
            for i in range(bottom-1, top-1, -1): # reverse order
                result.append(matrix[i][left])
            left += 1
        return result
            