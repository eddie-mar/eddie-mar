from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefix = strs[0]

        for word in strs[1:]:
            if not prefix:
                return ''
            i = 0
            while i < len(word) and i < len(prefix) and word[i] == prefix[i]:
                i += 1
            prefix = prefix[:i]
        
        return prefix


if __name__ == '__main__':
    a = ['flower', 'flow', 'flight']
    b = ['dog', 'racecar', 'car']
    c = ['residual', 'result', 'resolution', 'resolve', 'restitution']

    test = Solution()
    a = test.longestCommonPrefix(a)
    b = test.longestCommonPrefix(b)
    c = test.longestCommonPrefix(c)

    print(a)
    print(b)
    print(c)