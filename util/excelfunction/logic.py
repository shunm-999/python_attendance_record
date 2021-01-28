from util.excelfunction.excel_function import ExcelFunction


class AND(ExcelFunction):
    def __init__(self, *conditions):
        self.conditions = conditions

    def __str__(self):
        condition_str = ', '.join(str(value) for value in self.conditions)
        return f'AND({condition_str})'


class OR(ExcelFunction):
    def __init__(self, *conditions):
        self.conditions = conditions

    def __str__(self):
        condition_str = ', '.join(str(value) for value in self.conditions)
        return f'OR({condition_str})'


class NOT(ExcelFunction):
    def __init__(self, condition):
        self.condition = condition

    def __str__(self):
        return f'NOT({self.condition})'


class IF(ExcelFunction):

    def __init__(self, condition, true_value, false_value=None):
        self.condition = condition
        self.true_value = true_value
        self.false_value = false_value

    def __str__(self):
        if self.false_value is None:
            return f'IF({self.condition}, {self.true_value})'
        else:
            return f'IF({self.condition}, {self.true_value}, {self.false_value})'


class IF_ERROR(ExcelFunction):

    def __init__(self, target, error_value):
        self.target = target
        self.error_value = error_value

    def __str__(self):
        return f'IFERROR({self.target}, {self.error_value})'


class IS_BLANK(ExcelFunction):
    def __init__(self, target):
        self.target = target

    def __str__(self):
        return f'ISBLANK({self.target})'


class IS_NOT_BLANK(ExcelFunction):
    def __init__(self, target):
        self.target = target

    def __str__(self):
        return NOT(IS_BLANK(self.target)).to_str()
