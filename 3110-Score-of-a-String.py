class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for index in range(len(s)):
            if index != (len(s) - 1):
                score = score + abs(ord(s[index]) - ord(s[index + 1]))
        return score
