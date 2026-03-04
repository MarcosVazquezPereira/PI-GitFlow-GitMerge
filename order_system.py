from datetime import datetime

jslfjsdjfosdjfo
class Order:
    def __init__(self, order_id, customer, items, discount=0):
        self.order_id = order_id
        self.customer = customer
        self.items = items  # list of dicts: {"name": str, "price": float, "qty": int}
        self.discount = discount
        self.created_at = datetime.now()

    def total_price(self):
        subtotal = sum(item["price"] * item["qty"] for item in self.items)

        if self.discount < 0 or self.discount > 100:
            raise ValueError("Invalid discount")

        return subtotal * (1 - self.discount / 100)

    def summary(self):
        return {
            "order_id": self.order_id,
            "customer": self.customer,
            "total": round(self.total_price(), 2),
            "discount": self.discount,
            "items": sum(item["qty"] for item in self.items),
        }


class OrderManager:
    def __init__(self):
        self.orders = {}

    def create_order(self, order_id, customer, items, discount=0):
        if order_id in self.orders:
            raise ValueError("Order already exists")

        order = Order(order_id, customer, items, discount)
        self.orders[order_id] = order
        return order

    def get_order(self, order_id):
        return self.orders.get(order_id)

    def get_total_revenue(self):
        return sum(order.total_price() for order in self.orders.values())


if __name__ == "__main__":
    manager = OrderManager()

    manager.create_order(
        1,
        "Alice",
        [
            {"name": "Keyboard", "price": 50, "qty": 1},
            {"name": "Mouse", "price": 25, "qty": 2},
        ],
        discount=10,
    )

    print(manager.get_total_revenue())
