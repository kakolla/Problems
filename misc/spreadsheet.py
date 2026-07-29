









class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0 for _ in range(26)] for _ in range(rows)]
        self.rows = rows
        

    def setCell(self, cell: str, value: int) -> None:
        letter = cell[0]
        number = int(cell[1:])
        self.grid[number-1][ord(letter) - ord('A')] = value

        

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)
        

    def getCell(self, cell: str) -> int:
        letter = cell[0]
        number = int(cell[1:])
        return self.grid[number-1][ord(letter) - ord('A')]

    def getValue(self, formula: str) -> int:
        """=X+Y"""
        plus = formula.find("+")
        a = formula[1:plus]
        b = formula[plus+1:]


        if not a[0].isnumeric():
            a = self.getCell(a)

        if not b[0].isnumeric():
            b = self.getCell(b)

        return int(a) + int(b)

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)











class Spreadsheet:

    def __init__(self, rows: int):
        self.grid = [[0 for _ in range(26)] for _ in range(rows)]
        self.rows = rows
        

    def setCell(self, cell: str, value: int) -> None:
        letter = cell[0]
        number = int(cell[1:])
        self.grid[number-1][ord(letter) - ord('A')] = value

        

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)
        

    def getCell(self, cell: str) -> int:
        letter = cell[0]
        number = int(cell[1:])
        return self.grid[number-1][ord(letter) - ord('A')]

    def getValue(self, formula: str) -> int:
        """=X+Y"""
        plus = formula.find("+")
        a = formula[1:plus]
        b = formula[plus+1:]


        if not a[0].isnumeric():
            a = self.getCell(a)

        if not b[0].isnumeric():
            b = self.getCell(b)

        return int(a) + int(b)

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)

