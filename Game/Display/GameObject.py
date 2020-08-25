from .Screen import Screen

from dataclass import dataclass, field
from typing import Any
from abc import


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
    

class GameObject:

    def __init__(self, priority)
        self.priority = priority
        self.prioritized_item = Prioritized(priority, self)
        Screen.game_objects.put(self.prioritized_item)
        
    def render(self):
        pass
