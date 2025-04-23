# brute force
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPalindrome = ('', 0)
        size = len(s)
        if size == 1: return s

        for idx in range(size):
            for right_idx in range(idx + 1, size):
                subString = s[idx: right_idx + 1]
                if subString != subString[-1::-1]:
                    continue
                if len(subString) > longestPalindrome[1]:
                    longestPalindrome = (subString, len(subString))
        
        return longestPalindrome[0]


          
class Solution:
    def expandAroundCenter(self, left_idx, right_idx, s, longestPalindrome):
        while left_idx >= 0 and right_idx < len(s) and s[left_idx] == s[right_idx]:
            lenSubstring = right_idx + 1 - left_idx
            if lenSubstring > longestPalindrome[1]:
                longestPalindrome = (s[left_idx: right_idx + 1], lenSubstring)
            left_idx -= 1
            right_idx += 1
        return longestPalindrome

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        longestPalindrome = ('', 0)

        for idx in range(len(s)):
            longestPalindrome = self.expandAroundCenter(idx, idx, s, longestPalindrome) # for odd length
            longestPalindrome = self.expandAroundCenter(idx, idx + 1, s, longestPalindrome) # for even
        
        return longestPalindrome[0]