from app import db
from app.models import ProductQuestionModel
import os
import random
from werkzeug.utils import secure_filename
from .base_service import BaseService

class ProductQuestionService(BaseService):
    def __init__(self) -> None:
        super().__init__(ProductQuestionModel)

    
