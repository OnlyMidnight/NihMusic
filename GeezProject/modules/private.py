# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
from GeezProject.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from GeezProject.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL,BOT_USERNAME, OWNER
logging.basicConfig(level=logging.INFO)

@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Haii {message.from_user.first_name} saya adalah {PROJECT_NAME}\n
🎤 **Saya Adalah Bot Music Group** 🎶\n
Dan Saya Di Kelola Oleh Ari, Dan saya Bisa Memutar Lagu di Voice Chat Group Anda.Dan Saya Memiliki Fitur Seperti :
• Mencari Dan Memutar Musik Yang Kamu Inginkan.
• Mendownload Lagu Yang Ingin Kamu Download,Dan
• Mendonasi Kan Ke Owner Bot Se Ikhlas nya,Jika Kamu Kelebihan Uang.

🌹 Special Thanks To : ᴠɪᴄᴋʏ X ᴀʀɪ 🌹

☕ Di Kelola Oleh : [ᴀʀɪ](https://t.me/SilenceSpe4ks)

""",

# Edit Yang Seharusnya Lu Edit Aja:D
# Tapi Jangan di Hapus Special Thanks To nya Yaaa :'D

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📓ʙᴀᴄᴀ ᴀᴛᴜʀᴀɴ ᴘᴀᴋᴀɪ ❗", url=f"https://telegra.ph/Panduan-Stereo-Musik-07-23-4")],
                [
                    InlineKeyboardButton(
                        "🌻 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"), 
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴘs 🌹", url=f"https://t.me/{SUPPORT_GROUP}")
                ],[
                    InlineKeyboardButton(
                        "☕ ᴅᴏɴᴀᴛᴇ", url=f"https://t.me/SilenceSpe4ks")
                ]
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = 'Next »', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton("➕ ᴛᴀᴍʙᴀʜᴋᴀɴ ᴀᴋᴜ ᴅɪ ɢʀᴏᴜᴘ ᴋᴀᴍᴜ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = '🌻 ᴄʜᴀɴɴᴇʟ', url=f"https://t.me/{UPDATES_CHANNEL}"),
             InlineKeyboardButton(text = 'ɢʀᴏᴜᴘs 🌹', url=f"https://t.me/{SUPPORT_GROUP}")],
            [InlineKeyboardButton(text = '☕ ᴅᴏɴᴀᴛᴇ', url=f"https://t.me/SilenceSpe4ks")],
            [InlineKeyboardButton(text = '«', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '«', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '»', callback_data = f"help+{pos+1}")
            ],
        ]
    return button


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ **Apakah Anda ingin mencari Link YouTube?**",
        reply_markup=InlineKeyboardMarkup(
            [   
                [    
                    InlineKeyboardButton(
                        "✅ Ya", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Tidak ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        """**Klik Tombol dibawah untuk Melihat Cara Menggunakan Bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📄 ᴄᴀʀᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ʙᴏᴛ 📄", url="https://telegra.ph/Panduan-Stereo-Musik-07-23-4"
                    )
                ]
            ]
        ),
    )  


@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
async def reload(client: Client, message: Message):
    await message.reply_text("""✅ Bot **berhasil dimulai ulang!**\n\n• **Daftar admin** telah **diperbarui**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☕ ᴄʀᴇᴀᴛᴇᴅ", url=f"https://t.me/SilenceSpe4ks"
                    ),
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴘs 🌹", url=f"https://t.me/luciddreaams"
                    )
                ]
            ]
        )
   )

