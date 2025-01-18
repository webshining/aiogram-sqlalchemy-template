from abc import ABC, abstractmethod

from aiogram.filters.callback_data import CallbackQueryFilter, CallbackData
from aiogram.utils.keyboard import InlineKeyboardMarkup
from aiogram.utils.magic_filter import MagicFilter


class BaseKeyboardABC(ABC):
    @property
    @abstractmethod
    def filter(self, rule: MagicFilter | None = None) -> CallbackQueryFilter:
        pass

    @property
    @abstractmethod
    def keyboard(self) -> InlineKeyboardMarkup:
        pass

    @classmethod
    def _get_data(cls, **kwargs) -> str:
        return cls.Callback(**kwargs).pack()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, 'Callback') or not issubclass(cls.Callback, CallbackData):
            raise TypeError(
                f"{cls.__name__} должен содержать вложенный класс 'Callback', наследующийся от CallbackData."
            )
