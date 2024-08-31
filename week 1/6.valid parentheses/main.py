class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        closeToOpen = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack


s = Solution()
print(s.isValid("({["))
