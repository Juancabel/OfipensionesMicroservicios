from fastapi import APIRouter, status, Body
import informes.logic.informes_logic as informes_service
from models.models import Informe, InformeOut, InformeCollection

router = APIRouter()
ENDPOINT_NAME = "/informes"


@router.get(
    "/",
    response_description="List all informes",
    response_model=InformeCollection,
    status_code=status.HTTP_200_OK,
)
async def get_informes():
    return await informes_service.get_informes()


@router.get(
    "/{informe_code}",
    response_description="Get a single informe by its code",
    response_model=InformeOut,
    status_code=status.HTTP_200_OK,
)
async def get_informe(informe_code: str):
    return await informes_service.get_informe(informe_code)


@router.post(
    "/",
    response_description="Create a new informe",
    response_model=InformeOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_informe(informe: Informe = Body(...)):
    return await informes_service.create_informe(informe)


@router.put(
    "/{informe_code}",
    response_description="Update an informe",
    response_model=InformeOut,
    status_code=status.HTTP_200_OK,
)
async def update_informe(informe_code: str, informe: Informe = Body(...)):
    return await informes_service.update_informe(informe_code, informe)


@router.delete(
    "/{informe_code}",
    response_description="Delete an informe",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_informe(informe_code: str):
    return await informes_service.delete_informe(informe_code)
