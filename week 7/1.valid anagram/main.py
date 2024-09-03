import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = dict()
        t_dict = dict()
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        return s_dict == t_dict

    def isAnagram_2(self,s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCount = collections.Counter(s)
        tCount = collections.Counter(t)
        for char in sCount:
            if char not in tCount:
                return False
            if sCount[char] != tCount[char]:
                return False
        return True



s = Solution()
a = 'tale'
b = 'late'
print(s.isAnagram(a, b))
print(s.isAnagram_2(a, b))
