from flask import render_template, redirect, url_for, request, jsonify
from app.services import ConversationService
from datetime import datetime
from app.auth import get_current_user


class ConversationController:
    def __init__(self) -> None:
        self.conversation_service = ConversationService()    

    def get(self):
        # conversations =  self.conversation_service.get()
        return render_template("admin/conversation/index.html")
    
    def get_conversation_data(self):
        # Determine the column to sort by
        columns = ["id", "staff_id", "user_id","created_by","created_at","updated_by","updated_at"]
        data = self.conversation_service.get(request, columns)
        return jsonify(data)
    
    def create(self):
        prev_conversation=self.conversation_service.get_by_user_id(get_current_user().id)
        if prev_conversation:
            my_conversation=prev_conversation
        else:
            my_conversation=self.conversation_service.create(
                user_id=get_current_user().id,
                created_by= get_current_user().id,
                created_at = datetime.now()
            )
        return redirect(url_for("conversation.index",my_conversation=my_conversation))

    def status(self,id):
        conversation = self.conversation_service.get_by_id(id)
        if conversation is None:
            return {"status":"error","message":"Conversation Not Found"}
        is_active=self.conversation_service.status(id)
        if is_active:
            return {"status":"success","message":"Conversation Activated","data":is_active}
        return {"status":"success","message":"Conversation Deactivated","data":is_active}