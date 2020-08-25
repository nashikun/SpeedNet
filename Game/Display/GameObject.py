from .Screen import Screen

from dataclass import dataclass, field
from typing import Any


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
    

class GameObject:
    priority = 100

    def __init__(self)
        self.prioritized_item = Prioritized(self.priority, self)
        Screen.game_objects.put(self.prioritized_item)
        
    def render(self):
        pass
