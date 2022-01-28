from typing import Optional, List

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    Text,
    DateTime,
    func,
    select,
    text,
)

from contactos_back.domain.colectivo import Colectivo
from contactos_back.domain.database_interface import DatabaseInterface

metadata = MetaData()

colectivos = Table(
    "colectivos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("nombre", Text, nullable=False),
    Column("fecha_creacion", DateTime, nullable=False, server_default=func.now()),
    Column(
        "fecha_modificacion",
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    ),
)


class MySQLDatabase(DatabaseInterface):
    def __init__(self, database_uri: str) -> None:
        self.engine = create_engine(database_uri)
        self.metadata = metadata
        self.metadata.create_all(self.engine)

    def get_all_colectivos(self) -> List[Colectivo]:
        connection = self.engine.connect()
        result = connection.execute(text("SELECT * FROM colectivos"))
        colectivos = [
            Colectivo(
                id=row[0],
                nombre=row[1],
                fecha_creacion=row[2],
                fecha_modificacion=row[3],
            )
            for row in result
        ]
        connection.close()
        return colectivos

    def get_colectivo(self, id: int) -> Optional[Colectivo]:
        connection = self.engine.connect()
        result = connection.execute(select([colectivo]).where(colectivo.c.id == id))
        row = result.fetchone()
        if row:
            colectivo = Colectivo(
                id=row[0],
                nombre=row[1],
                fecha_creacion=row[2],
                fecha_modificacion=row[3],
            )
        else:
            colectivo = None
        connection.close()
        return colectivo

    def create_colectivo(self, colectivo: Colectivo) -> Colectivo:
        connection = self.engine.connect()
        result = connection.execute(
            colectivo.insert().values(
                nombre=colectivo.nombre,
                fecha_creacion=colectivo.fecha_creacion,
                fecha_modificacion=colectivo.fecha_modificacion,
            )
        )
        colectivo.id
