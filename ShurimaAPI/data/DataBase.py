from abc import ABC
from typing import Dict

class DataBase(ABC):
    def __init__(self, src: Dict) -> None:
        self._src = src

    def __str__(self) -> str:
        return ", ".join(f"{str(k)}: {str(v)}" for k, v in vars(self).items() if k not in ['_src'])
