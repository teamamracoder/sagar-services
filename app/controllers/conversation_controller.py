from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateConversationForm
from app.forms import UpdateConversationForm
from app.services import ConversationService



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
        form = CreateConversationForm()
        if form.validate_on_submit():
            self.conversation_service.create(
                staff_id=form.staff_id.data,
                user_id=form.user_id.data,
                created_by= 2,
            )
            return redirect(url_for("conversation.index"))
        return render_template("admin/conversation/add.html", form=form)
    
    def update(self,id):
        form = UpdateConversationForm()
        conversation = self.conversation_service.get_by_id(id)
        if conversation is None:
            return render_template("admin/error/something_went_wrong.html")
        if form.validate_on_submit():
            self.conversation_service.update(
                id,
                staff_id=form.staff_id.data,
                user_id=form.user_id.data,
            )
            return redirect(url_for("conversation.index"))
        form.staff_id.data=conversation.staff_id
        form.user_id.data=conversation.user_id
        return render_template("admin/conversation/update.html",id=id, form=form)

    def status(self,id):
        conversation = self.conversation_service.get_by_id(id)
        if conversation is None:
            return render_template("admin/error/something_went_wrong.html")
        self.conversation_service.status(id)
        return redirect(url_for("conversation.index"))