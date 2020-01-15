class Solution:
    def isValid(self, s):
        if s=="" or s==None:
            return True
        
        parentheses_stack = []
        opening_parentheses = ["(","{","["]
        closing_parentheses = [")","}","]"]
        
        for parentheses in s:
            if parentheses in opening_parentheses:
                parentheses_stack.append(parentheses)
            elif len(parentheses_stack) == 0:
                return False
            else:
                poped_parentheses = parentheses_stack.pop()
                if  opening_parentheses.index(poped_parentheses) != closing_parentheses.index(parentheses):
                    return False
        return True if len(parentheses_stack)==0 else False
                    