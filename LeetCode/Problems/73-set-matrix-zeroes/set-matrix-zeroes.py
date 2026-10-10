# m * n 2차원 배열이 주어졌을 때 0이 있으면 해당 셀의 행,열의 모든 셀을 0으로 바꿔라
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()

        m = len(matrix[0])
        n = len(matrix)
        for y in range(n):
            for x in range(m):
                if matrix[y][x] == 0:
                    rows.add(x)
                    cols.add(y)
        
        print(rows, cols)

        for y in range(n):
            for x in range(m):
                if y in cols or x in rows:
                    matrix[y][x] = 0