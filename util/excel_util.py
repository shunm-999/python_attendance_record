from openpyxl.utils import get_column_letter


class ExcelUtil:
    @staticmethod
    def create_range_string(start_row, start_column, end_row, end_column):
        if type(start_column) is int:
            start_column = get_column_letter(start_column)

        if type(end_column) is int:
            end_column = get_column_letter(end_column)

        return f'{start_column}{start_row}:{end_column}{end_row}'
