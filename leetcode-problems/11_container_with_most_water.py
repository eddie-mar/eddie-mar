class Solution:
    def movePointer(self, idx, direction, height):
        next_pointer = idx + direction
        while height[idx] > height[next_pointer] and (next_pointer < len(height) or next_pointer > 0):
            next_pointer += direction

        return next_pointer

    def maxArea(self, height: List[int]) -> int:
        if len(height) == 1:
            return None

        maxArea = 0
        left_idx = 0
        right_idx = len(height) - 1

        while left_idx < right_idx:
            min_height_idx = left_idx if height[left_idx] < height[right_idx] else right_idx
            area = (right_idx - left_idx) * (height[min_height_idx])
            if area > maxArea: maxArea = area
            
            if min_height_idx == left_idx:
                left_idx = self.movePointer(left_idx, 1, height)
            elif min_height_idx == right_idx:
                right_idx = self.movePointer(right_idx, -1, height)

        return maxArea

