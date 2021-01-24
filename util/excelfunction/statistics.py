from util.excelfunction.excel_function import ExcelFunction


class COUNT_IF(ExcelFunction):
    def __init__(self, cell_range: str, condition: str):
        self.cell_range = cell_range
        self.condition = condition

    def __str__(self):
        return f'COUNTIF({self.cell_range}, {self.condition})'
