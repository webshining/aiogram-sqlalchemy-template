from .inter import i18n_middleware
from .user import UserMiddleware

middlewares = [UserMiddleware(), i18n_middleware]

__all__ = ["middlewares"]
