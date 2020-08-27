from .screen import Screen

from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any = field(compare=False)


class GameObject:
    priority = 100

    def __init__(self):
        self.prioritized_item = PrioritizedItem(self.priority, self)
        Screen.game_objects.put(self.prioritized_item)

    def render(self):
        pass
