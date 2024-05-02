from flask import render_template,session
from app.utils import VOICEUtils
import random
class ErrorController:

    def page_not_found(self):
        # otp= random.randint(10000,99999)
        # session['otp']=otp
        # voice = VOICEUtils()
        # success = voice.voice_send("9749276281", otp)
        # print(f"Message sent successfully: {success}")
        return render_template("error/page_not_found.html")

    def something_went_wrong(self):
        return render_template("error/something_went_wrong.html")

    def unauthorized_access(self):
        return render_template("error/unauthorized_access.html")

    def deactivated(self):
        return render_template("error/deactivated.html")
