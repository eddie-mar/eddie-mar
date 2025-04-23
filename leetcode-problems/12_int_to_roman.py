class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        int_val = 0
        prev = 0
        
        for char in s[-1::-1]:
            convert = values.get(char)
            if convert < prev:
                int_val -= convert
                continue
            int_val += convert
            prev = convert

        return int_val
