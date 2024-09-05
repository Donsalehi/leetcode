class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4,
               1
               ]

        symbols = ['M', 'CM', 'D', 'CD',
                   'C', 'XC', 'L', 'XL',
                   'X', 'IX', 'V', 'IV',
                   'I'
                   ]

        ans = ''
        i = 0
        while num > 0:
            while num >= val[i]:
                ans += symbols[i]
                num -= val[i]

            i += 1

        return ans


s = Solution()
num = 3749
print(s.intToRoman(num))
