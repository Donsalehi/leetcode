class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        ans = list()
        start = end = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    ans.append(str(end))
                else:
                    ans.append(f'{start}->{end}')
                start = end = nums[i]

        if start == end:
            ans.append(str(end))
        else:
            ans.append(f'{start}->{end}')

        return ans


s = Solution()
nums = [0, 2, 3, 4, 6, 8, 9]
print(s.summaryRanges(nums))
