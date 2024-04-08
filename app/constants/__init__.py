# constant class


class Constant:
    def __init__(self, data: dict) -> None:
        self.data = data

    def get_key(self, val: str) -> int:
        for key, value in self.data.items():
            if value == val:
                return key

    def get_value(self, key: int) -> str:
        return self.data.get(key)
    
    def get_all_items(self) -> list:
        return list(self.data.items())

    def get_all_keys(self) -> list:
        return list(self.data.keys())

    def get_all_values(self) -> list:
        return list(self.data.values())

    def get_all_items_as_dict(self) -> dict:
        return self.data

# constant data

payment_methods = Constant({1: "COD", 2: "ONLINE_PAYMENT"})

roles = Constant({1: "ADMIN", 2: "STAFF", 3: "CUSTOMER"})

order_statuses = Constant(
    {
        1: "PROCESSING",
        2: "PACKAGING",
        3: "SHIPPING",
        4: "DELIVERED",
        5: "ON_THE_WAY",
        6: "RETURNED",
        7: "CANCELLED",
    }
)

discount_types = Constant({1: "CASH", 2: "PERCENTAGE"})

service_statuses = Constant(
    {
        1: "BOOKED",
        2: "ON_THE_WAY",
        3: "PROVIDED",
        4: "CANCELLED",
        5: "PENDING",
        6: "RESCHEDULED",
    }
)

cart_statuses = Constant({1: "ADDED", 2: "ORDERED", 3: "REMOVED"})

departments = Constant(
    {
        1: "SALES",
        2: "MARKETING",
        3: "ACCOUNTING",
        3: "REPAIRING",
        4: "PC_BUILDING"
    }
)

payment_statuses = Constant({1: "PAID", 2:"PENDING", 3:"REFUNDED", 4:"FAILED"})