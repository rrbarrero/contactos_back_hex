import pytest
from sqlalchemy import literal_column
from sqlalchemy.engine import Connection

from contactos_back.adapters.database.mysql import colectivos, MySQLDatabase
from contactos_back.domain.colectivo import Colectivo


@pytest.fixture
def database(database_uri: str) -> MySQLDatabase:
    return MySQLDatabase(database_uri)


@pytest.fixture
def colectivos_fixtures(database_connection: Connection) -> [Colectivo]:
    database_connection.execute(
        colectivos.insert(),
        [
            {"id": 1, "nombre": "Colectivo 1"},
            {"id": 2, "nombre": "Colectivo 2"},
            {"id": 3, "nombre": "Colectivo 3"},
        ],
    )
    result = database_connection.execute(colectivos.select())
    return [Colectivo(**row) for row in result]


class TestMysqlAdapter:
    def test_get_colectivos(
        self, database: MySQLDatabase, colectivos_fixtures: [Colectivo]
    ):
        assert database.get_all_colectivos() == colectivos_fixtures
