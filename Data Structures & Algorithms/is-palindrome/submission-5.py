class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.is_alnum(s[l]):
                l += 1
            while l < r and not self.is_alnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True

    def is_alnum(self, c):
        ord_c = ord(c)
        return (
            ord('A') <= ord_c <= ord('Z') or
            ord('a') <= ord_c <= ord('z') or
            ord('0') <= ord_c <= ord('9')
        )