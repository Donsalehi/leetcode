from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_rn = {}
        dict_m = {}
        for char in set(ransomNote):
            dict_rn[char] = ransomNote.count(char)
        for char in set(magazine):
            dict_m[char] = magazine.count(char)
        for char in dict_rn:
            if char not in dict_m:
                return False
            if dict_rn[char] > dict_m[char]:
                return False
        return True

    def canConstruct_2(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char not in magazine:
                return False
            magazine = magazine.replace(char, " ", 1)
        return True

    def canConstruct_3(self, ransomNote: str, magazine: str) -> bool:
        note_counter = Counter(ransomNote)
        mag_counter = Counter(magazine)
        for char, count in note_counter.items():
            if mag_counter[char] < count:
                return False
        return True


s = Solution()
ransomNote = "aa"
magazine = "aab"
print(s.canConstruct(ransomNote, magazine))
print(s.canConstruct_2(ransomNote, magazine))
print(s.canConstruct_3(ransomNote, magazine))
