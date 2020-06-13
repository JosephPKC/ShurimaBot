from abc import ABC
from typing import Dict

class DataBase(ABC):
    """ DataBase is the base container for all data containers.
    """
    def __init__(self, src: Dict) -> None:
        """ Constructor for the DataBase data container.

        Args:
            src (Dict): The source JSON from which the data container retrieves data from.
        """
        self._src = src

    def __str__(self) -> str:
        return ", ".join(f"{str(k)}: {str(v)}" for k, v in vars(self).items() if k not in ['_src'])
