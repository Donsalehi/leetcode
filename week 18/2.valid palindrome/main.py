import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_copy = ''.join(char.lower() for char in s if char.isalnum())
        return s_copy == s_copy[::-1]

    def isPalindrome2(self, s: str) -> bool:
        s = s.lower().replace(" ", "")
        s = re.sub(r'[^a-zA-Z0-9]+', "", s)
        return s == s[::-1]


solution = Solution()
s = "A man, a plan, a canal: Panama"
print("first way:", solution.isPalindrome(s))
print("second way:", solution.isPalindrome2(s))
