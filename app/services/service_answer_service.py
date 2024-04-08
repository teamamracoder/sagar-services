from app.models import ServiceAnswerModel
from .base_service import BaseService

class ServiceAnswerService(BaseService):
    def __init__(self) -> None:
        super().__init__(ServiceAnswerModel)

    # def add_service_question_with_answer(self, datas: list) -> list:
    #     for data in datas:
    #         # Retrieve answer details for each service ID
    #         answer = self.get_answer_details_by_service_id(data["service_id"])
    #         # Add answer to the question
    #         if answer:
    #             data["answer"] = answer
    #         else:
    #             data["answer"] = "Unknown"  # Provide a default value if answer is missing
    #     return datas

    # def get_answer_details_by_service_id(self, service_id):
    #     # Retrieve answer details for a given service ID from the database
    #     answer = ServiceAnswerModel.query.filter_by(service_id=service_id).first()
    #     if answer:
    #         return answer.answer  # Return answer if found
    #     else:
    #         return "No Answer Found"  # Return a default message if no answer is found
