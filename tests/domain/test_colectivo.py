from typing import List

from datetime import datetime
from unittest.mock import Mock

import inject
import pytest

from contactos_back.domain.actions.get_all_colectivos import GetAllColectivos
from contactos_back.domain.colectivo import Colectivo
from contactos_back.domain.database_interface import DatabaseInterface


@pytest.fixture
def database() -> Mock:
    return Mock(spec=DatabaseInterface)


@pytest.fixture
def injector(database: Mock) -> None:
    inject.clear_and_configure(lambda binder: binder.bind(DatabaseInterface, database))


@pytest.fixture
def colectivos() -> List[Colectivo]:
    return [
        Colectivo(
            id=1,
            nombre="Colectivo 1",
            fecha_creacion=datetime.now(),
            fecha_modificacion=datetime.now(),
        ),
        Colectivo(
            id=2,
            nombre="Colectivo 2",
            fecha_creacion=datetime.now(),
            fecha_modificacion=datetime.now(),
        ),
    ]


class TestColectivos:
    def test_get_all_colectivos(
        self, injector: None, database: Mock, colectivos: List[Colectivo]
    ) -> None:
        database.get_all_colectivos.return_value = colectivos
        get_all_colectivos = GetAllColectivos()
        assert get_all_colectivos.execute() == colectivos
