import random


def isBadVersion(version: int, first_bad_version: int) -> bool:
    return version >= first_bad_version


class Solution:
    def firstBadVersion(self, n: int, first_bad_version: int) -> int:
        start, end = 1, n
        while start != end:
            mid = (start + end) // 2
            if isBadVersion(mid, first_bad_version):
                end = mid
            else:
                start = mid + 1
        return start


s = Solution()
n = 5
first_bad_version = random.randint(1, n)
print(f"we have {n} version.")
print("the first bad version is:", first_bad_version)
print("our answer is:", s.firstBadVersion(n, first_bad_version))
