from flask import render_template


class AuthController:

    def login(self):
        return render_template("auth/login.html")

    def signup(self):
        return render_template("auth/signup.html")

    def reset_password(self):
        return render_template("auth/reset_password.html")
