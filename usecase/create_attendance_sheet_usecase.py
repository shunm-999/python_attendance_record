from abc import abstractmethod

from data.user_input_data import UserInputData
from usecase.use_case import UseCase


class CreateAttendanceSheetUseCase(UseCase):

    @abstractmethod
    def invoke(self, input_data: UserInputData):
        pass
