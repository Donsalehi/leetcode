class Solution:
    def isHappy(self, n: int) -> bool:
        numb = n
        seen = set()
        while numb != 1 and numb not in seen:
            seen.add(numb)
            sum_p = 0
            digits = str(numb)
            for digit in digits:
                sum_p += int(digit) ** 2
            numb = sum_p
        if numb == 1:
            return True
        else:
            return False


s = Solution()
print(s.isHappy(2))
