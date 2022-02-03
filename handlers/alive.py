import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/30868ddf51d5599e8c777.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
Hᴇʟʟᴏ ɪ ᴀᴍ sᴜᴘᴇʀ ғᴀsᴛ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍs ɢʀᴏᴜᴘs...
┏━━━━━━━━━━━━━━━━━┓
┣★ Uᴘᴅᴀᴛᴇs : [Dᴇᴍᴏɴ Cʀᴇᴀᴛᴏʀs](https://t.me/The_Superiour_Network)
┣★ Sᴜᴘᴘᴏʀᴛ : [Wᴏʀʟᴅ FʀɪᴇɴᴅSʜɪᴘ Zᴏɴᴇ](https://t.me/World_FriendShip_Zone)
┣★ Oᴡɴᴇʀ   : [Sᴜᴍɪᴛ Yᴀᴅᴀᴠ](https://t.me/Simple_Mundaa)
┣★ Fᴇᴍᴀʟᴇ Oᴡɴᴇʀ : [Nɪᴋɪᴛᴀ](https://t.me/Cute_Shezhadi012)
┗━━━━━━━━━━━━━━━━━┛
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "Sumit"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/30868ddf51d5599e8c777.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/World_FriendShip_Zone")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["DarkxMusic","Sumit", "#Channel", "@Channel", "/Channel", "Channel"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/65be304b45005b8bd84db.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Uᴘᴅᴀᴛᴇs", url=f"https://t.me/Demon_Creators")
                ]
            ]
        ),
    )
