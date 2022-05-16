from fastapi.routing import APIRouter

from .resources.health_check import health_check_route

router = APIRouter(prefix="/api/v1")
router.include_router(health_check_route)
