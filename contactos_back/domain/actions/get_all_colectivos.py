from typing import List

import inject

from contactos_back.domain.colectivo import Colectivo
from contactos_back.domain.database_interface import DatabaseInterface


class GetAllColectivos:
    @inject.autoparams()
    def __init__(self, database: DatabaseInterface):
        self.__database_interface = database

    def execute(self) -> List[Colectivo]:
        return self.__database_interface.get_all_colectivos()
