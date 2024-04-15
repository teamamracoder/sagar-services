from flask import render_template, redirect, url_for, request, jsonify
from app.services import ConversationService, UserService
from datetime import datetime
from app.auth import get_current_user
from app.forms import CreateConversationForm

class ConversationController:
    def __init__(self) -> None:
        self.conversation_service = ConversationService()    
        self.user_service = UserService()

    def get(self):
        # conversations =  self.conversation_service.get()
        return render_template("admin/conversation/index.html")
    
    def get_conversation_data(self):
        # Determine the column to sort by
        columns = ["id", "staff_id", "user_id","created_by","created_at","updated_by","updated_at"]
        data = self.conversation_service.get(request, columns)
        data = self.user_service.add_user_with_this(data)
        return jsonify(data)
    
    def create(self):
        form=CreateConversationForm()
        logged_in_user,roles=get_current_user().values()
        if form.validate_on_submit():
            prev_conversation=self.conversation_service.get_by_user_id(form.user_id.data)
            if prev_conversation:
                return render_template("admin/conversation/add.html", form=form, error="Conversation already exists with that user")
            
            self.conversation_service.create(
                user_id=form.user_id.data,
                created_by= logged_in_user.id,
                created_at = datetime.now()
            )
            return redirect(url_for("conversation.index"))
        return render_template("admin/conversation/add.html", form=form)

    def status(self,id):
        conversation = self.conversation_service.get_by_id(id)
        if conversation is None:
            return {"status":"error","message":"Conversation Not Found"}
        is_active=self.conversation_service.status(id)
        if is_active:
            return {"status":"success","message":"Conversation Activated","data":is_active}
        return {"status":"success","message":"Conversation Deactivated","data":is_active}