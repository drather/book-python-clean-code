from typing import Union

class DispatchedOrder:
    """
    방금 수신한 배달 주문
    """
    status = "dispatched"

    def __init__(self, when):
        self._when = when

    def message(self) -> dict:
        return {
            "status": self.status,
            "msg": "주문 시각 {0}".format(
                self._when.isoformat()
            ),
        }


class OrderInTransition:
    """
    배달 중인 주문
    """
    status = "in transit"

    def __init__(self, current_location):
        self._current_location = current_location

    def message(self) -> dict:
        return {
            "status": self.status,
            "msg": "배달중, 현재 위치: {0}".format(
                self._current_location()
            ),
        }


class OrderDelivered:
    """
    배달 중인 주문
    """
    status = "delivered"

    def __init__(self, delivered_at):
        self._delivered_at = delivered_at

    def message(self) -> dict:
        return {
            "status": self.status,
            "msg": "배달 완료 시각: {0}".format(
                self._delivered_at.isoformat()
            ),
        }


class DeliveryOder:
    def __init__(self, delivery_id: str, status: Union[DispatchedOrder, OrderInTransition, OrderDelivered]) -> None:
        self._delivery_id = delivery_id
        self._status = status

    def message(self) -> dict:
        return {
            "id": self._delivery_id,
            **self._status.message()
        }