class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s = dict()
        mapping_t = dict()

        for char_s, char_t in zip(s, t):
            if char_s in mapping_s:
                if mapping_s[char_s] != char_t:
                    return False
            else:
                mapping_s[char_s] = char_t

            if char_t in mapping_t:
                if mapping_t[char_t] != char_s:
                    return False
            else:
                mapping_t[char_t] = char_s
        return True


solution = Solution()
s = 'badc'
t = 'baba'
print(solution.isIsomorphic(s, t))
