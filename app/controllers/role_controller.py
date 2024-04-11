from flask import render_template, redirect, url_for, request, jsonify
from app.services import RoleService, StaffService
from app.auth import get_current_user
from datetime import datetime

class RoleController:

    def __init__(self) -> None:
        self.role_service = RoleService()
        self.staff_service = StaffService()

    def create(self,role_key,user_id):
        role=self.role_service.get_role_by_user_id_and_role_key(role_key,user_id)
        #no role found, create a role
        if role is None:
            if role_key==2:
                return redirect(url_for("staff.add",user_id=user_id))
            
            self.role_service.create(
                user_id=user_id, 
                role=role_key,
                created_by=get_current_user().id,
                created_at=datetime.now()
            )
            return redirect(url_for("user.index"))
        
        #role found, so change is_active
        self.status(role.id)
        return redirect(url_for("user.index"))
    
    def status(self,id):
        role=self.role_service.get_by_id(id)
        self.role_service.status(id)
        staff=self.staff_service.get_by_user_id(role.user_id)
        if role.role==2:
            self.staff_service.status(staff.id)
        return redirect(url_for("user.index"))