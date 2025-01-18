from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.utils.magic_filter import MagicFilter

from loader import i18n
from .base import BaseKeyboardABC


class LangKeyboard(BaseKeyboardABC):
    @property
    def filter(self, rule: MagicFilter | None = None):
        return self.Callback.filter(rule)

    @property
    def keyboard(self):
        builder = InlineKeyboardBuilder()

        for lang in i18n.available_locales:
            builder.button(text=lang.upper(), callback_data=self._get_data(lang=lang))
        builder.adjust(3)

        return builder.as_markup()

    class Callback(CallbackData, prefix="lang"):
        lang: str


LangKeyboard = LangKeyboard()
