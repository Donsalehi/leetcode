class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        mapping = {'2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz'}

        queue = ['']

        for digit in digits:
            letters = mapping[digit]
            new_queue = []

            for combination in queue:
                for letter in letters:
                    new_queue.append(combination + letter)

            queue = new_queue

        return queue

    def letterCombinations1(self, digits: str) -> list[str]:
        if not digits:
            return []

        mapping = {'2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz'}

        def backtrack(sub_digits):
            if len(sub_digits) == 1:
                return [i for i in mapping[sub_digits]]

            characters = [i + j for i in mapping[sub_digits[0]] for j in backtrack(sub_digits[1:])]
            return characters

        return backtrack(digits)


s = Solution()
digits = "23"
print(s.letterCombinations(digits))
