from decimal import Decimal
from datetime import datetime
from dataclasses import dataclass


@dataclass()
class UserInfo:
    user_id: int
    first_name: str
    last_name: str
    username: str
    money: Decimal
    last_updated: datetime
    active: bool

@dataclass()
class UserCode:
    user_id: int
    code: str
