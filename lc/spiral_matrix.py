class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m, n = len(matrix), len(matrix[0])
        top, down, left, right = 0, m-1, 0, n-1
        i, j = 0, 0
        res = []
        direction = 0
        while top <= down and left <= right:
            if direction == 0:
                res.append(matrix[i][j])
                j += 1
                if j > right:
                    direction = (direction + 1) % 4
                    i += 1
                    j -= 1
                    top += 1
            elif direction == 1:
                res.append(matrix[i][j])
                i += 1
                if i > down:
                    direction = (direction + 1) % 4
                    i -= 1
                    j -= 1
                    right -= 1
            elif direction == 2:
                res.append(matrix[i][j])
                j -= 1
                if j < left:
                    direction = (direction + 1) % 4
                    j += 1
                    i -= 1
                    down -= 1
            elif direction == 3:
                res.append(matrix[i][j])
                i -= 1
                if i < top:  
                    direction = (direction + 1) % 4
                    i += 1
                    j += 1
                    left += 1
        return res

    def print(self, matrix: list[list[int]]):
        for item in matrix:
            print(item)


if __name__ == "__main__":
    so = Solution()
    so.print(so.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    