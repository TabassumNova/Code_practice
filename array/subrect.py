class SubrectangleQueries:

    def __init__(self, rectangle: list[list[int]]):
        self.rectangle = rectangle
        pass
    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                self.rectangle[0][r][c] = newValue
        pass
    def getValue(self, row: int, col: int) -> int:
        val = self.rectangle[0][row][col]
        return val

if __name__ == "__main__":
    # ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
    # Your SubrectangleQueries object will be instantiated and called as such:
    rectangle = [[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
    obj = SubrectangleQueries([[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]])
    param_2 = obj.getValue(0,2)
    obj.updateSubrectangle(0, 0, 3, 2, 5)
    pass