class Solution:
    def removeStars(self, s: str) -> str:
        s = list(s)
        stack = []
        for l in s:
            if l != "*":
                stack.append(l) 
            else:
                stack.pop()
        
        return ''.join(stack)

        