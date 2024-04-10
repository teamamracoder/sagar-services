from flask import render_template
from app.auth import get_current_user

class DashboardController:

    def dashboard(self):
        return render_template("admin/dashboard.html", user=get_current_user())
