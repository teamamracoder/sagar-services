from flask import render_template


class ErrorController:

    def page_not_found(self):
        return render_template("error/page_not_found.html")

    def something_went_wrong(self):
        return render_template("error/something_went_wrong.html")

    def unauthorized_access(self):
        return render_template("error/unauthorized_access.html")
