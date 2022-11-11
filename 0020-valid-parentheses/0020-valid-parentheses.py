class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {'(':')', '{':'}','[':']'}
        
        if len(s) % 2: return False # odd string cant be true
        
        for i in s: # iterate through the string
            if i in hashMap: 
                # if it's in the left bracket we append it to stack like
                # (, {, [ 
                stack.append(i)
            # empty stack or left bracket doesnt match ({[ (in stack) 
            # doesnt match i which is )}] since if it does exist it will be
            # appended alr by up thing
            elif len(stack) == 0 or hashMap[stack.pop()] != i:
                return False
        return len(stack) == 0 # will be true
        
        
        