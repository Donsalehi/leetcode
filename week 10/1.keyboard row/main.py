class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set("zxcvbnm")

        ans = []

        for word in words:
            w = set(word.lower())
            if w.issubset(row1) or w.issubset(row2) or w.issubset(row3):
                ans.append(word)

        return ans


s = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"]
print(s.findWords(words))
