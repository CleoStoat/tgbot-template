from dataclasses import dataclass
from typing import Callable

@dataclass
class HandlerModel:
    priority: int

@dataclass
class CommandModel(HandlerModel):
    callback: Callable
    name: str
    description: str
    hidden: bool = False