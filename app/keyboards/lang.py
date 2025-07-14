from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

from loader import i18n


class LangKeyboard(CallbackData, prefix="lang"):
    lang: str

    @staticmethod
    def keyboard():
        builder = InlineKeyboardBuilder()

        for lang in i18n.available_locales:
            builder.button(
                text=lang.capitalize(),
                callback_data=LangKeyboard(lang=lang).pack(),
            )
        builder.adjust(3)

        return builder.as_markup()
