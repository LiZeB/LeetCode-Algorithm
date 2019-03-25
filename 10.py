class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = p
        text = s
        if not pattern:
            return not text
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])

##https://www.jianshu.com/p/85f3e5a9fcda
