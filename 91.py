class Solution:
    def numDecodings(self, s: str) -> int:
        s = '0' + s
        length = len(s)
        dp = [1] * (length)

        for i in range(1, length):
            c = 0
            single = s[i]  # 一位数
            if single != '0':
                c += dp[i - 1]
            double = s[i - 1:i + 1]  # 两位数
            if (not double.startswith('0')) and 0 < int(double) < 27:
                c += dp[i - 2]
            dp[i] = c
        return dp[-1]
