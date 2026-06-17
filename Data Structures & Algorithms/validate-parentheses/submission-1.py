class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if not stack and (i == ']' or i==')' or i=='}'):
                return False
            if i == '[' or i=='(' or i=='{':
                stack.append(i)
                continue
            if stack[-1] == '(' and  i == ')':
                stack.pop()
                continue
            elif stack[-1] == '[' and  i == ']':
                stack.pop()
                continue
            elif stack[-1] == '{' and  i == '}':
                stack.pop()
                continue
            else:
                return False
        if not stack:
            return True
        else:
            return False