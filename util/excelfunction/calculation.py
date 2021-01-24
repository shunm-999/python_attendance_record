from util.excelfunction.excel_function import ExcelFunction


class SUM(ExcelFunction):

    def __init__(self, *targets):
        self.targets = targets

    def __str__(self):
        target = ', '.join(str(value) for value in self.targets)
        return f'SUM({target})'
