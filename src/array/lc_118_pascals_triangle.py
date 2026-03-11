from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Method 1: Using Recursion
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        previous_rows = self.generate(numRows=numRows - 1)
        current_row = [1] * numRows

        for i in range(1, numRows - 1):
            current_row[i] = previous_rows[-1][i - 1] + previous_rows[-1][i]

        previous_rows.append(current_row)
        return previous_rows

    # def generate(self, numRows: int) -> List[List[int]]:
    #     """
    #     Method 2: Using Combinatorial Formula
    #     """
    #     result: List = []

    #     if numRows == 0:
    #         return result

    #     first_row = [1]
    #     result.append(first_row)

    #     for i in range(1, numRows):
    #         previous_row = result[i - 1]
    #         current_row = [1]

    #         for j in range(1, i):
    #             current_row.append(previous_row[j - 1] + previous_row[j])

    #         current_row.append(1)
    #         result.append(current_row)

    #     return result

    # def generate(self, numRows: int) -> List[List[int]]:
    #     """
    #     Method 3: Using Dynamic Programming with 1D Array
    #     """
    #     if numRows == 0:
    #         return []
    #     if numRows == 1:
    #         return [[1]]

    #     previous_rows = self.generate(numRows - 1)
    #     previous_row = previous_rows[-1]
    #     current_row = [1]

    #     for i in range(1, numRows - 1):
    #         current_row.append(previous_row[i - 1] + previous_row[i])

    #     current_row.append(1)
    #     previous_rows.append(current_row)

    #     return previous_rows
