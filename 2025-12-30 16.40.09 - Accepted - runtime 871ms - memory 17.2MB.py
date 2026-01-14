class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high + 1):
            s = str(num)
            n = len(s)
            # Only check even digit numbers
            if n % 2 == 0:
                half = n // 2
                first_half_sum = sum(int(d) for d in s[:half])
                second_half_sum = sum(int(d) for d in s[half:])
                if first_half_sum == second_half_sum:
                    count += 1
        return count