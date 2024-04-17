from flask import render_template


class PrivacyPolicyController:

    def privacy_policy_page(self):
        return render_template("customer/privacy_policy.html")