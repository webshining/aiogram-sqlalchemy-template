from .status import StatusMiddleware

middlewares = [StatusMiddleware()]

__all__ = ["middlewares"]
