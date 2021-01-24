from abc import ABCMeta


class ExcelFunction(metaclass=ABCMeta):
    def to_str(self):
        return str(self)
