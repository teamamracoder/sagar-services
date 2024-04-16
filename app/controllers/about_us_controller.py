from flask import render_template

class AboutUsController:
    ## customer controllers ##

    def customer_get(self):
        return render_template("customer/about_us.html")