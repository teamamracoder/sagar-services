from flask import render_template, redirect, url_for, request, jsonify
from app.forms import CreateMessageForm
from app.services import MessageService, UserService
from app.services import ConversationService
from datetime import datetime
from app.auth import get_current_user
from app.utils import FileUtils

class MessageController:
    def __init__(self) -> None:
        self.message_service = MessageService()
        self.conversation_service = ConversationService()
        self.user_service = UserService()

    def get(self,conversation_id):
        logged_in_user,roles=get_current_user().values()
        form = CreateMessageForm()
        conversation=self.conversation_service.get_by_id(conversation_id)
        messages=self.message_service.get_by_conversation_id(conversation_id)
        messages=self.user_service.add_message_with_this(messages)
        messages=self.message_service.add_attachement_url_with_this(messages)
        return render_template("admin/message/index.html",messages=messages,conversation=conversation, form=form, current_user=logged_in_user)


    def create(self,conversation_id):
        logged_in_user,roles=get_current_user().values()
        form = CreateMessageForm()
        if form.validate_on_submit():
            filepath=FileUtils.save('messages',[form.attachement_url.data])
            self.message_service.create(
                conversation_id=conversation_id,
                message=form.message.data,
                created_by=logged_in_user.id,
                created_at = datetime.now(),
                attachement_url=filepath
            )
            self.conversation_service.update(
                conversation_id,
                updated_at = datetime.now()
            )
            return redirect(url_for("message.index",conversation_id=conversation_id))
        return render_template("admin/message/add.html",conversation_id=conversation_id, form=form)


    def status(self,id,conversation_id):
        message = self.message_service.get_by_id(id)
        if message is None:
            return render_template("admin/error/something_went_wrong.html")
        self.message_service.status(id)
        return redirect(url_for("message.index",conversation_id=conversation_id))

    def chatbox(self):
        logged_in_user,roles=get_current_user().values()
        try:

            conversation=self.conversation_service.get_by_user_id(logged_in_user.id)
            if conversation:
                columns = ["id", "message", "attachement_url","conversation_id","created_at", "created_by"]
                messages=self.message_service.get_by_conversation_id_json(conversation.id,columns)
                messages=self.user_service.add_username_with_this(messages)
                for message in messages:
                    message['current_user_id']=logged_in_user.id
                return jsonify(messages)
            else:
                return {"status":"sucess","message":"write a message"}

        except Exception as e:
            return {"status":"failed","message":"something went wrong"}

    def write(self):
        logged_in_user,roles=get_current_user().values()
        conversation=self.conversation_service.get_by_user_id(logged_in_user.id)
        if not conversation:
            conversation = self.conversation_service.create(
                user_id=logged_in_user.id,
                created_by= logged_in_user.id,
                created_at = datetime.now()
            )
        filepath=FileUtils.save('messages',[request.files.get("attachement_url")])
        message = self.message_service.create(
            conversation_id=conversation.id,
            message=request.form.get("message"),
            created_by=logged_in_user.id,
            created_at = datetime.now(),
            attachement_url=filepath
        )
        self.conversation_service.update(
            conversation.id,
            updated_at = datetime.now()
        )
        if message:
            return {"status":"success","message":"message sent"}
        return {"status":"fail","message":"message sending failed"}