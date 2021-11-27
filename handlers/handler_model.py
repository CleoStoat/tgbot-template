from dataclasses import dataclass
from typing import Callable, Optional

@dataclass
class HandlerModel:
    priority: int

@dataclass
class CommandModel(HandlerModel):
    name: str
    description: str
    hidden: bool = False
    callback: Callable = None
