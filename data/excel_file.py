import openpyxl

from data.excel_sheet import ExcelSheet


class ExcelFile:
    def __init__(self, filename: str, create_file=False):
        self.filename = filename
        self.excel_sheet_list = []
        if create_file:
            self.workbook = openpyxl.Workbook(filename)
        else:
            self.workbook = openpyxl.load_workbook(filename)

        for worksheet in self.workbook.worksheets:
            excelSheet = ExcelSheet(worksheet)
            self.excel_sheet_list.append(excelSheet)

    def __str__(self):
        description = f'{self.filename} \n'
        description += '\n'.join(
            [f'{index} : {sheetname}' for index, sheetname in enumerate(self.workbook.sheetnames)])
        return description


class ExcelFileFactory:
    @staticmethod
    def load(filename):
        return ExcelFile(filename=filename, create_file=False)

    @staticmethod
    def create(filename):
        return ExcelFile(filename=filename, create_file=True)
