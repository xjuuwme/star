""" coding """


class PascalTriangle:
    """ Yang Triangle """

    @classmethod
    def generate(cls, num_rows):
        """ iterate the current and add the offset """
        res = [[1]]
        for _ in range(1, num_rows):
            res += [list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))]
        return res[:num_rows]


if __name__ == "__main__":
    print(PascalTriangle.generate(5))
