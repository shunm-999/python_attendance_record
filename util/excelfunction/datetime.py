from util.excelfunction.excel_function import ExcelFunction


class DATE(ExcelFunction):

    def __init__(self, year, month, day=1):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f'DATE({self.year}, {self.month}, {self.day})'


class YEAR(ExcelFunction):

    def __init__(self, year):
        self.year = year

    def __str__(self):
        return f'YEAR({self.year})'


class MONTH(ExcelFunction):

    def __init__(self, month):
        self.month = month

    def __str__(self):
        return f'MONTH({self.month})'


class DAY(ExcelFunction):

    def __init__(self, day):
        self.day = day

    def __str__(self):
        return f'DAY({self.day})'
