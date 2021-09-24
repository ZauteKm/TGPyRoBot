from pyrogram import (
    Client,
    filters
)
from tgpyrobot import (
    COMMAND_HAND_LER,
    DB_URI,
)
from tgpyrobot.helper_functions.cust_p_filters import admin_fliter
if DB_URI is not None:
    import tgpyrobot.helper_functions.sql_helpers.welcome_sql as sql


@Client.on_message(
    filters.command(["clearwelcome", "resetwelcome"], COMMAND_HAND_LER) &
    admin_fliter
)
async def clear_note(_, message):
    status_message = await message.reply_text(
        "checking 🤔🙄🙄",
        quote=True
    )
    sql.rm_welcome_setting(message.chat.id)
    await status_message.edit_text(
        "welcome message cleared from current chat."
    )
