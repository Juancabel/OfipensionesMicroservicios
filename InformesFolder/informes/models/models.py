# Models for the informes microservice

from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from typing import List
from models.db import PyObjectId


class InformeType(str, Enum):
    Classroom = "classroom"
    Laboratory = "laboratory"
    Auditorium = "auditorium"
    Office = "office"


class Informe(BaseModel):
    code: str = Field(...)
    capacity: int = Field(...)
    type: InformeType = Field(...)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "code": "ML515",
                "capacity": 50,
                "type": InformeType.Classroom,
            }
        },
    )


class InformeOut(Informe):
    id: PyObjectId = Field(alias="_id", default=None, serialization_alias="id")
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "64b9f1f4f1d2b2a3c4e5f6a7",
                "code": "ML515",
                "capacity": 50,
                "type": InformeType.Classroom,
            }
        },
    )


class InformeCollection(BaseModel):
    # A collection of informes
    informes: List[InformeOut] = Field(...)
