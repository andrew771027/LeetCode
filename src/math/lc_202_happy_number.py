class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_of_squares(num: int) -> int:
            total = 0

            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10

            return total

        slow = n
        fast = n

        while True:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))

            if slow == fast:
                break

        return slow == 1

    def is_happy_oracle(self, n: int) -> int:
        seen: set[int] = set()

        while n != 1 and n not in seen:
            seen.add(n)

            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return n == 1
