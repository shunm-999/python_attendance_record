from collections import Iterable

from openpyxl.styles import Font, Side, Border, PatternFill
from openpyxl.utils import get_column_letter, column_index_from_string
from openpyxl.worksheet.datavalidation import DataValidation


class ExcelSheet:
    MAX_ROW = 1048576

    def __init__(self, worksheet):
        self.worksheet = worksheet

    def get(self, row, column):
        if type(column) is str:
            column = column_index_from_string(column)
        return self.worksheet.cell(row=row, column=column).value

    def get_rows(self, start_row, start_column, end_row=None, end_column=None):
        cell_range = self.create_range_string(
            start_row=start_row,
            start_column=start_column,
            end_row=end_row,
            end_column=end_column)

        values = []
        for row in self.worksheet[cell_range]:
            row_value = []
            for col in row:
                row_value.append(col.value)
            values.append(row_value)

        return values

    def put(self, row, column, value):
        if type(column) is str:
            column = column_index_from_string(column)
        self.worksheet.cell(row=row, column=column).value = value

    def put_rows(self, start_row, start_column, end_row=None, end_column=None, values=None):
        if values is None:
            values = [[]]
        if not isinstance(values, Iterable):
            return

        if not isinstance(values[0], Iterable):
            return

        cell_range = self.create_range_string(
            start_row=start_row,
            start_column=start_column,
            end_row=end_row,
            end_column=end_column)

        for row_num, row in enumerate(self.worksheet[cell_range]):
            for column_num, col in enumerate(row):
                col.value = values[row_num][column_num]

    def insert_rows(self, row):
        self.worksheet.insert_rows(row)

    def delete_rows(self, row):
        self.worksheet.delete_rows(row)

    def insert_columns(self, column):
        if type(column) is str:
            column = column_index_from_string(column)
        self.worksheet.insert_cols(column)

    def delete_columns(self, column):
        if type(column) is str:
            column = column_index_from_string(column)
        self.worksheet.delete_cols(column)

    def get_row_height(self, row) -> int:
        return self.worksheet.row_dimensions[row].height

    def set_row_height(self, row, height):
        self.worksheet.row_dimensions[row].height = height

    def get_column_width(self, column) -> int:
        if type(column) is int:
            column = get_column_letter(column)
        return self.worksheet.column_dimensions[column].width

    def set_column_width(self, column, width):
        if type(column) is int:
            column = get_column_letter(column)
        self.worksheet.column_dimensions[column].width = width

    def merge_cells(self, start_row, start_column, end_row, end_column):

        merge_cell_range = self.create_range_string(
            start_row=start_row,
            start_column=start_column,
            end_row=end_row,
            end_column=end_column)

        self.worksheet.merge_cells(merge_cell_range)

    def merge_cells_and_dimensions(self, start_row, start_column, end_row, end_column):
        height = 0
        width = 0

        for row_num in range(start_row, end_row + 1):
            height += self.get_row_height(row=row_num)
        for column_num in range(start_column, end_column + 1):
            width += self.get_column_width(column=column_num)

        self.merge_cells(start_row=start_row, start_column=start_column, end_row=end_row, end_column=end_column)
        self.set_row_height(row=start_row, height=height)
        self.set_column_width(column=start_column, width=width)

    def set_freeze_panes(self, row, column):
        if type(column) is int:
            column = get_column_letter(column)

        self.worksheet.freeze_panes = f'{column}{row}'

    def get_font(self, row, column) -> Font:
        if type(column) is str:
            column = column_index_from_string(column)
        return self.worksheet.cell(row=row, column=column).font

    def set_font(self, row, column, size=None, bold=None, italic=None):
        if type(column) is str:
            column = column_index_from_string(column)
        self.worksheet.cell(row=row, column=column).font = Font(size=size, bold=bold, italic=italic)

    def set_ruled_line(self, start_row, start_column, end_row=None, end_column=None, style='thin', color='000000'):

        if end_row is None:
            end_row = start_row
        if end_column is None:
            end_column = end_column

        side = Side(style=style, color=color)
        border = Border(top=side, bottom=side, left=side, right=side)

        if type(start_column) is str:
            start_column = column_index_from_string(start_column)
        if type(end_column) is str:
            end_column = column_index_from_string(end_column)

        for row_num in range(start_row, end_row + 1):
            for column_num in range(start_column, end_column + 1):
                self.worksheet.cell(row=row_num, column=column_num).border = border

    def get_pattern_fill(self, row, column) -> PatternFill:
        if type(column) is str:
            column = column_index_from_string(column)

        return self.worksheet.cell(row=row, column=column).fill

    def set_pattern_fill(self,
                         start_row,
                         start_column,
                         end_row=None,
                         end_column=None,
                         pattern_type='solid',
                         fg_color='d3d3d3'):
        if end_row is None:
            end_row = start_row
        if end_column is None:
            end_column = end_column

        if type(start_column) is str:
            start_column = column_index_from_string(start_column)
        if type(end_column) is str:
            end_column = column_index_from_string(end_column)

        fill = PatternFill(patternType=pattern_type, fgColor=fg_color)

        for row_num in range(start_row, end_row + 1):
            for column_num in range(start_column, end_column + 1):
                self.worksheet.cell(row=row_num, column=column_num).fill = fill

    def set_data_validation(self, start_row, end_row, column, formula=None):
        if formula is None:
            formula = []

        if end_row is None:
            end_row = ExcelSheet.MAX_ROW

        formula = ','.join(formula)
        dv = DataValidation(type="list", formula1=formula)

        dv.ranges = self.create_range_string(
            start_row=start_row,
            start_column=column,
            end_row=end_row,
            end_column=column)

        self.worksheet.add_data_validation(dv)

    @staticmethod
    def convert_num_to_alpha(number):
        return get_column_letter(number)

    @staticmethod
    def convert_alpha_to_num(alphabet):
        return column_index_from_string(alphabet)

    @staticmethod
    def create_range_string(start_row, start_column, end_row, end_column):
        if type(start_column) is int:
            start_column = get_column_letter(start_column)

        if type(end_column) is int:
            end_column = get_column_letter(end_column)

        return f'{start_column}{start_row}:{end_column}{end_row}'
