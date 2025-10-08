from typing import List

# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            if i == 0:
                triangle.append([1])
                continue
            row = [1] * (i + 1)
            for j in range(i + 1):
                if j == 0 or j == i:
                    continue
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)

if __name__ == '__main__':
    x = Solution()
    print(x.generate(10))
