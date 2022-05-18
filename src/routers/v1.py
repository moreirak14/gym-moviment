from fastapi.routing import APIRouter

from .resources.health_check import health_check_route
from .resources.user import user_route

router = APIRouter(prefix="/api/v1")
router.include_router(health_check_route)
router.include_router(user_route)
