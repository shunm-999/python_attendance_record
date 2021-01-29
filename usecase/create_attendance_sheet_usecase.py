from abc import abstractmethod

from data.user_input_data import UserInputData
from repository.excel_repository_interface import ExcelRepositoryInterface
from usecase.use_case import UseCase


class CreateAttendanceSheetUseCase(UseCase):

    def __init__(self, excel_repository: ExcelRepositoryInterface):
        pass

    @abstractmethod
    def invoke(self, input_data: UserInputData):
        pass
