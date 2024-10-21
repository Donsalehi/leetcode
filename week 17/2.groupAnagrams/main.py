class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_dict = {}

        # we can also use defaultdict() in collections library that create an empty list when the key is not in defaultdict()
        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word not in anagram_dict:
                anagram_dict[sorted_word] = []

            anagram_dict[sorted_word].append(word)

        return list(anagram_dict.values())


s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs))
