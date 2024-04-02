from app import db
from app.models import CategoryModel
import os
import random
from werkzeug.utils import secure_filename
from .base_service import BaseService

class CategoryService(BaseService):
    def __init__(self) -> None:
        super().__init__(CategoryModel)

    
