class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7

        # Group consecutive characters
        groups = []
        prev = word[0]
        count = 1
        for ch in word[1:]:
            if ch == prev:
                count += 1
            else:
                groups.append(count)
                prev = ch
                count = 1
        groups.append(count)

        max_len = len(word)
        dp = [0] * (max_len + 1)
        dp[0] = 1  # 0 groups, 0 length, 1 way

        for cnt in groups:
            new_dp = [0] * (max_len + 1)
            prefix = [0] * (max_len + 2)
            for l in range(max_len + 1):
                prefix[l + 1] = (prefix[l] + dp[l]) % MOD
            for l in range(1, max_len + 1):
                left = max(0, l - cnt)
                right = l - 1
                new_dp[l] = (prefix[right + 1] - prefix[left]) % MOD
            dp = new_dp

        return sum(dp[k:]) % MOD
