from db import db
from app.models import RoleModel
from .base_service import BaseService


class RoleService(BaseService):
    def __init__(self) -> None:
        super().__init__(RoleModel)
