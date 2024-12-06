"""
This module contains the logic for the informes app.
Main functions:
- get_informes: Get a list of all informes
- get_informe: Get a single informe
- create_informe: Create a new informe
- update_informe: Update an informe
- delete_informe: Delete an informe
"""

from models.models import Informe, InformeCollection
from models.db import informe_collection
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException


async def get_informes():
    """
    Get a list of informes
    :return: A list of informes
    """
    informes = await informe_collection.find().to_list(1000)
    return InformeCollection(informes=informes)


async def get_informe(informe_code: str):
    """
    Get a single informe
    :param informe_code: The code of the informe
    :return: The informe
    """
    if (informe := await informe_collection.find_one({"code": informe_code})) is not None:
        return informe

    raise HTTPException(
        status_code=404, detail=f"Informe with code {informe_code} not found"
    )


async def create_informe(informe: Informe):
    """
    Insert a new informe record.
    """

    try:
        new_informe = await informe_collection.insert_one(
            informe.model_dump(by_alias=True, exclude=["id"])
        )
        created_informe = await informe_collection.find_one({"_id": new_informe.inserted_id})
        return created_informe

    except DuplicateKeyError:
        raise HTTPException(
            status_code=409, detail=f"Informe with code {informe.code} already exists"
        )


async def update_informe(informe_code: str, informe: Informe):
    """
    Update an informe
    :param informe_code: The code of the informe
    :param informe: The informe data
    :return: The updated informe
    """

    try:
        update_result = await informe_collection.update_one(
            {"code": informe_code},
            {"$set": informe.model_dump(by_alias=True, exclude=["id"])},
        )
        if update_result.modified_count == 1:
            if (
                updated_informe := await informe_collection.find_one({"code": informe.code})
            ) is not None:
                return updated_informe
    except DuplicateKeyError:
        raise HTTPException(
            status_code=409, detail=f"Informe with code {informe.code} already exists"
        )

    raise HTTPException(
        status_code=404,
        detail=f"Informe with code {informe_code} not found or no updates were made",
    )


async def delete_informe(informe_code: str):
    """
    Delete an informe
    :param informe_code: The code of the informe
    """
    delete_result = await informe_collection.delete_one({"code": informe_code})

    if delete_result.deleted_count == 1:
        return

    raise HTTPException(
        status_code=404, detail=f"Informe with code {informe_code} not found"
    )
