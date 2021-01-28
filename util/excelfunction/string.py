from enum import Enum

from util.excelfunction.excel_function import ExcelFunction


class TEXT(ExcelFunction):
    def __init__(self, number, text_format):
        self.number = number
        self.text_format = text_format

    def __str__(self):
        text_format = self.text_format.value if isinstance(self.text_format, TextFormat) else self.text_format
        return f'TEXT({self.number}, "{text_format}")'


class TextFormat(Enum):
    DAY_OF_WEEK = 'aaaa'
    DAY_OF_WEEK_SHORT = 'aaa'
    DAY_OF_WEEK_ENGLISH = 'ddd'
