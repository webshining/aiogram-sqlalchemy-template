from .admins import middlewares as admins_middlewares
from .users import middlewares as users_middlewares

middlewares = [users_middlewares, admins_middlewares]

__all__ = ["middlewares"]
