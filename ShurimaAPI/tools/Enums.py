from enum import Enum
from typing import Optional

class LOLRegion(Enum):
    NA = "na1"

class LOLClashPosition(Enum):
    UNSELECTED = "UNSELECTED"
    FILL = "FILL"
    TOP = "TOP"
    JUNGLE = "JUNGLE"
    MIDDLE = "MIDDLE"
    BOTTOM = "BOTTOM"
    UTILITY = "UTILITY"

class LOLClashRole(Enum):
    CAPTAIN = "CAPTAIN"
    MEMBER = "MEMBER"
