from flask import render_template


class HomeController:

    def homepage(self):
        return render_template("customer/home.html")
