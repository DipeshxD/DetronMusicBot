from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAADBQADoQQAAnzQIFXIf_60wEnGEwI")
    await message.reply_text(
        f"""**Hey, I'm {bn} π΅

I can play music in your group's voice call. Developed by [πΏπππππ](https://t.me/DIPESH_XD).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π  Source Code π ", url="https://github.com/xdipesh/DetronMusicBot")
                  ],[
                    InlineKeyboardButton(
                        "π¬ Group", url="https://t.me/BEST_FRIENDS69"
                    ),
                    InlineKeyboardButton(
                        "π Channel", url="https://t.me/AboutDipesh"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "βIF ANY PROBLEM CLICK HEREβ", url="https://t.me/DIPESH_XD"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π Channel", url="https://t.me/AboutDipesh")
                ]
            ]
        )
   )


