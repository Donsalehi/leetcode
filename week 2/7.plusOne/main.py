class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1
        while digits[i] == 9 and i >= 0:
            digits[i] = 0
            i -= 1
        if i == -1:
            digits.insert(0, 1)
        else:
            digits[i] += 1
        return digits

    def anotherPlusOne(self, digits: list[int]) -> list[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        digits.insert(0, 1)
        return digits


s = Solution()
digits = [3, 9, 9]
print(digits)
s.plusOne(digits)
print(digits)
s.anotherPlusOne(digits)
print(digits)
