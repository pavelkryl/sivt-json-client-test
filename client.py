from abc import ABC, abstractmethod
from typing import Any, Optional
from requests import Response
import requests
import logging

logger = logging.getLogger(__name__)

class Klient(ABC):


    @abstractmethod
    def get_items(self) -> dict[str, Any]:
        ...

    @abstractmethod
    def new_item(self, item: dict[str, Any]) -> Optional[dict[str,Any]]:
        ...

    @abstractmethod
    def delete_item(self, item_id: str) -> bool:
        ...



def test() -> None:
    # vytvoření instance klienta
    klient = Klient("192.168.88.83", 5000)

    # získání seznamu všech položek
    items = klient.get_items()
    print(items)

    new_item :dict [str,Any] = {
        "id": 10
        # TODO
    }

    resp_new = klient.new_item(new_item)
    print(f"odpoved na create_item: {resp_new}")

    items = klient.get_items()
    print(items)

    resp_delete = klient.delete_item("10")
    print(f"odpoved na remove_item: {resp_delete}")

    items = klient.get_items()
    print(items)

test()