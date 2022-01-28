import os
from typing import Optional

import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection

from contactos_back.adapters.database.mysql import metadata


@pytest.fixture
def database_uri() -> Optional[str]:
    # of type: mysql://username:password@server/db
    db_host = os.environ.get("DB_HOST")
    db_password = os.environ.get("DB_PASSWORD")
    db_port = os.environ.get("DB_PORT")
    db_name = os.environ.get("DB_DATABASE")
    return f"mysql://root:{db_password}@{db_host}:{db_port}/{db_name}"


@pytest.fixture
def database_connection(database_uri: str) -> Connection:
    engine = create_engine(database_uri)
    connection = engine.connect()
    for table in metadata.sorted_tables:
        connection.execute(table.delete())
    yield connection
