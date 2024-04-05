from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateMessageForm
from app.forms import UpdateMessageForm
from app.services import MessageService
from app.services import ConversationService
from datetime import datetime



class MessageController:
    def __init__(self) -> None:
        self.message_service = MessageService()    
        self.conversation_service = ConversationService()    

    def get(self):
        return render_template("admin/message/index.html")
    
    def get_message_data(self):
        # Determine the column to sort by
        columns = ["id", "conversation_id" "message_text","created_at","updated_at", "is_active"]
        
        data = self.message_service.get(request, columns)
        return jsonify(data)
    
    def create(self):
        form = CreateMessageForm()
        if form.validate_on_submit():
            self.message_service.create(
                conversation_id=form.conversation_id.data,
                message_text=form.message_text.data,
                created_by=1,
                created_at = datetime.now()
            )
            return redirect(url_for("message.index"))
        return render_template("admin/message/add.html", form=form)
    
    def update(self,id):
        message = self.message_service.get_by_id(id)
        form = UpdateMessageForm(obj = message)
        if message is None:
            return render_template("admin/error/something_went_wrong.html")
        if form.validate_on_submit():
            self.message_service.update(
                id,
                conversation_id=form.conversation_id.data,
                message_text=form.message_text.data,
                updated_by=1,
                updated_at = datetime.now()

            )
            return redirect(url_for("message.index"))
        return render_template("admin/message/update.html",id=id, form=form)

    def status(self,id):
        message = self.message_service.get_by_id(id)
        if message is None:
            return render_template("admin/error/something_went_wrong.html")
        self.message_service.status(id)
        return redirect(url_for("message.index"))