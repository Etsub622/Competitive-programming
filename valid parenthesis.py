class Solution:
    def isValid(self, s: str) -> bool:
        dici= {'(':')','{':'}','[':']'}
        stack=[]
        opening=['(','{','[']
        closing=[')','}',']']
        for char in s:
            if char in opening:
                stack.append(char)      
            else:
                if stack==[]:
                    return False
                else:
                  if dici[stack[-1]]==char:
                    stack.pop()
                  else:
                    return False     
        return stack==[]
