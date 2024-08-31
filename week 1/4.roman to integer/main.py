class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
                   'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000
                   }
        numb = 0
        prev = 0
        for char in s:
            value = mapping[char]
            if value > prev:
                numb += value - 2 * prev
            else:
                numb += value
            prev = value
        return numb


s = Solution()
print(s.romanToInt("MCMXCIV"))
