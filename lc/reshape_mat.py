def matrixReshape(nums, r, c):
    flat = sum(nums, [])
    if len(flat) != r * c:
        return nums
    tuples = zip(*([iter(flat)] * c))
    return map(list, tuples)


def matrixReshape11(mat: list[list[int]], r, c):
    return mat if len(sum(mat, [])) != r * c \
                else map(list, zip(*([iter(sum(mat, []))]*c)))


def matrixReshape2(mat, r: int, c: int):
    if len(mat) * len(mat[0]) != r*c:
        return mat
    res = []
    newrow = []
    i = 0
    for row in mat:
        for item in row:
            newrow.append(item)                
            if (i+1) % c == 0:
                res.append(newrow)
                newrow = []
            i += 1
    return res


mat = [[1, 2, 3, 4], [5, 6, 7, 8]]
res = matrixReshape11(mat, 4, 2)
flattened = sum(res, [])
print(flattened)


"""Java Solution """
"""
class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int m = mat.length;
        int n = mat[0].length;
        if (m*n != r*c)
            return mat;
        int[][] res = new int[r][c];
        for (int i = 0; i < m*n; i++) {
            res[i/c][i%c] = mat[i/n][i%n];
        }
        return res;
    }
}
"""