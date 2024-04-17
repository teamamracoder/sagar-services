from flask import Blueprint

from app.controllers import PrivacyPolicyController

privacy_policy_bp = Blueprint("privacy_policy", __name__)
privacy_policy_controller = PrivacyPolicyController()


@privacy_policy_bp.route("/privacy_policy/")
def privacy_policy():
    return privacy_policy_controller.privacy_policy_page()
