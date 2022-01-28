from dataclasses import dataclass
from datetime import datetime
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(frozen=True)
class Colectivo:
    id: int
    nombre: str
    fecha_creacion: datetime
    fecha_modificacion: datetime
