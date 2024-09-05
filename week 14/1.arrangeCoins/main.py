class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2
            current_sum = (mid * (mid + 1)) // 2

            if current_sum == n:
                return mid

            elif current_sum < n:
                left = mid + 1

            else:
                right = mid - 1

        return right


s = Solution()
n = 8
print(s.arrangeCoins(n))
