from enum import Enum
from typing import Optional

class LOL:
    class Region(Enum):
        NA = "na1"

    class ClashPosition(Enum):
        UNSELECTED = "UNSELECTED"
        FILL = "FILL"
        TOP = "TOP"
        JUNGLE = "JUNGLE"
        MIDDLE = "MIDDLE"
        BOTTOM = "BOTTOM"
        UTILITY = "UTILITY"

    class ClashRole(Enum):
        CAPTAIN = "CAPTAIN"
        MEMBER = "MEMBER"

    class Queue(Enum):
        asdf = ""