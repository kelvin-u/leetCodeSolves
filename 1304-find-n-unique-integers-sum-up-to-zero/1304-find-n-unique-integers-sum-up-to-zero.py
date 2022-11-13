class Solution:
    def sumZero(self, n: int) -> List[int]:
        array = []
        
        if n %2 != 0:
            array.append(0)
        
        for i in range(1, n, 2):
            array.extend([i, -i])
        
        return array
        