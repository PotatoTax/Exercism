class Matrix:
    def __init__(self, matrix_string):
        self.arr = [list(map(int, row.split())) for row in matrix_string.split("\n")]

    def row(self, index):
        return self.arr[index-1]

    def column(self, index):
        return [self.arr[i][index-1] for i in range(len(self.arr))]
