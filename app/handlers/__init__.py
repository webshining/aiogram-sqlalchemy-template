from .admins import router as admin_router
from .users import router as user_router

__all__ = ['admin_router', 'user_router']
