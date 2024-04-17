# email templates


class DefaultTemplate:
    def __init__(self, data: dict) -> None:
        self.data = data

    def get_key(self, val: str) -> str:
        for key, value in self.data.items():
            if value == val:
                return key

    def get_value(self, key: str) -> str:
        return self.data.get(key)
    



email_templates = DefaultTemplate(
        {
            "EMAIL_ORDER_COMPLETION":"value",
            "ACCOUNT_CREATION":"value"
        }
    )


"""
OTP
ACCOUNT CREATION
ORDER DELIVERY(SUCCESS)
ORDER CREATION +
    STATUS CHANGE
SERVICE BOOKED + 
    STATUS CHANGE
REVIEW ASKING EMAIL(ORDER,SERVICE BOOKING)
OFFER RELATED EMAIL 

INVOICE AFTER PAYMENT
"""