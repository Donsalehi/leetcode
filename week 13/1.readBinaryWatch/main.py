class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        result = []
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:
                    result.append(f'{h}:{m:02d}')

        return result


s = Solution()
turnedOn = 1
print(s.readBinaryWatch(turnedOn))
