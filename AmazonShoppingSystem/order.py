from __future__ import annotations
from datetime import datetime
from system_enums import OrderStatus

class OrderLog:
    order_id: str
    creation_date: datetime
    status: OrderStatus

    def __init__(self, order_id: str, creation_date: datetime, status: OrderStatus) -> None:
        self.order_id = order_id
        self.creation_date = creation_date
        self.status = status


class Order:
    order_id: str
    order_date: datetime
    status: OrderStatus
    order_log = []

    def __init__(self, order_id: str, order_date: datetime, status: OrderStatus) -> None:
        self.order_id = order_id
        self.order_date = order_date
        self.status = status
        self.order_log = []

    def add_order_log(self, order_log: OrderLog):
        self.order_log.append(order_log)

    def send_to_shipment(self):
        pass

    def make_payment(self):
        pass