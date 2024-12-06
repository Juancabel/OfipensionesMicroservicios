from fastapi import APIRouter

from views import informes_view

API_PREFIX = "/api"
router = APIRouter()

router.include_router(informes_view.router, prefix=informes_view.ENDPOINT_NAME)