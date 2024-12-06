# Models for the informes microservice

from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from typing import List
from models.db import PyObjectId

class Informe(BaseModel):
    descripcion: str = Field(...)
    al_dia: int = Field(...)
    code: str = Field(...)
    fecha: str = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "descripcion": "Este es un informe de prueba, en general todo esta bien",
                "al_dia": 50,
                "code": "INF01",
                "fecha": "12/12/2022",
            }
        },
    )


class InformeOut(Informe):
    id: PyObjectId = Field(alias="_id", default=None, serialization_alias="id")
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "descripcion": "Este es un informe de prueba, en general todo esta bien",
                "al_dia": 50,
                "code": "INF01",
                "fecha": "12/12/2022",
            }
        },
    )


class InformeCollection(BaseModel):
    # A collection of informes
    informes: List[InformeOut] = Field(...)
