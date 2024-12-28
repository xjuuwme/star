def matrixReshape(nums, r, c):
    flat = sum(nums, [])
    if len(flat) != r * c:
        return nums
    print()
    tuples = zip(*([iter(flat)] * c))
    return map(list, tuples)


def matrixReshape11(mat: list[list[int]], r, c):
    return mat if len(sum(mat, [])) != r * c \
                else map(list, zip(*([iter(sum(mat, []))]*c)))


def matrixReshapeFlat(nums, r: int, c: int) -> list[list[int]]:
    """ another normal way """
    if r * c != len(nums) * len(nums[0]):
        return nums
    else:
        items = [y for x in nums for y in x]
        return [items[x*c: x*c+c] for x in range(r)]


def matrixReshape2(mat, r: int, c: int):
    """my solution"""
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


def print_mat(matrix: list[list[int]]):
    """ print matrix 2d """
    for item in matrix:
        print(item)


mat = [[1, 2, 3, 4], [5, 6, 7, 8]]
r, c = 4, 2
res = matrixReshape11(mat, r, c)
print_mat(res)
flattened = sum(mat, [])
print(flattened)

"""Java Solution """

# class Solution {
#     public int[][] matrixReshape(int[][] mat, int r, int c) {
#         int m = mat.length;
#         int n = mat[0].length;
#         if (m*n != r*c)
#             return mat;
#         int[][] res = new int[r][c];
#         for (int i = 0; i < m*n; i++) {
#             res[i/c][i%c] = mat[i/n][i%n];
#         }
#         return res;
#     }
# }