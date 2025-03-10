def spiralOrder(matrix):
    return matrix and [*matrix.pop(0)] + spiralOrder([*zip(*matrix)][::-1])


def print_ma(matrix):
    for row in matrix:
        print(row)


a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
c = [1, 2, 3]
x = list(zip(a, b, c))
print("==========================")
for item in x:
    for ee in item:
        print(ee)
print("==========================")

ma = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
bb = [*ma.pop(0)]
cc = [ma.pop()]
print(bb)
print(cc)

zipped = [list(zip(*ma))[::-1]]
print_ma(zipped)
print_ma(zipped[::-1])

print("================Recursive Spiral Order of Matrix========================")
matt = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
print(spiralOrder(matt))