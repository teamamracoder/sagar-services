from flask import render_template

class AboutUsController:
    ## customer controllers ##

    def about_us_page(self):
        return render_template("customer/about_us.html")