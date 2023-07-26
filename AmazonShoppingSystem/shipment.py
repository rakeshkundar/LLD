from __future__ import annotations
from datetime import datetime
from system_enums import ShipmentStatus
from accounts.account import Account

class ShipmentLog:
    shipment_id: str
    shipment_date: datetime
    status: ShipmentStatus

    def __init__(self, id: str, shipment_date: datetime, status: ShipmentStatus) -> None:
        self.shipment_id = id
        self.shipment_date = shipment_date
        self.status = status


class Shipment:
    shipment_id: str
    shipment_date: datetime
    status: ShipmentStatus
    shipment_log: list(ShipmentLog)

    def __init__(self, id: str, shipment_date: datetime, status: ShipmentStatus) -> None:
        self.shipment_id = id
        self.shipment_date = shipment_date
        self.status = status
        self.shipment_log = []

    def add_shipment_log(self, log: ShipmentLog):
        self.shipment_log.append(log)


class Notification:
    notification_id: str
    message: str
    created_date: datetime

    def __init__(self, id: str, message: str) -> None:
        self.notification_id = id
        self.message = message
        self.created_date = datetime.now().date()

    def send_notification(self, account: Account):
        pass