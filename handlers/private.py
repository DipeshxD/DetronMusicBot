from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIYqWCf3bqhz7RrWf_4St57ydK4kLK7AAI-AwAC3O4AAVVRfNbcVZ0joh8E")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [𝘿𝙄𝙋𝙀𝙎𝙃](https://t.me/DIPESH_XD).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://github.com/xdipesh/DetronMusicBot")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/BEST_FRIENDS69"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/AboutDipesh"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "❗IF ANY PROBLEM CLICK HERE❗", url="https://t.me/DIPESH_XD"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/AboutDipesh")
                ]
            ]
        )
   )


