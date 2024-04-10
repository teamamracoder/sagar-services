from db import db
from app.models import CouponModel
from .base_service import BaseService


class CouponService(BaseService):
    def __init__(self) -> None:
        super().__init__(CouponModel)
