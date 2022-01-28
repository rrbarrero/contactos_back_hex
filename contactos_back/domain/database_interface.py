from abc import ABC, abstractmethod
from typing import Optional, List

from contactos_back.domain.colectivo import Colectivo


class DatabaseInterface(ABC):
    @abstractmethod
    def get_all_colectivos(self) -> List[Colectivo]:
        pass
