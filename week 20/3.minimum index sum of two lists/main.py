class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        dict1 = {v: i for i, v in enumerate(list1)}

        ans = []
        min_sum = float('inf')

        for j, v in enumerate(list2):
            if v in list1:
                index_sum = j + dict1[v]

                if index_sum < min_sum:
                    min_sum = index_sum
                    ans = [v]

                elif index_sum == min_sum:
                    ans.append(v)

        return ans


s = Solution()
list1 = ["happy", "sad", "good"]
list2 = ["sad", "happy", "good"]
print(s.findRestaurant(list1, list2))
