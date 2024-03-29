from flask import render_template


class DashboardController:

    def dashboard(self):
        return render_template("admin/dashboard.html")
