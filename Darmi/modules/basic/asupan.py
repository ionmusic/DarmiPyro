import asyncio
from asyncio import gather
from random import choice
from pyrogram import Client, filters, enums
from pyrogram.types import ChatPermissions, ChatPrivileges, Message
from pyrogram import Client as gez
from darmilibs.darmi.helper import edit_or_reply, get_text, ReplyCheck
from darmilibs import DEVS, BL_GCAST
from darmilibs.darmi.helper.cmd import *
from Darmi.modules.basic import add_command_help
from config import *
from Darmi import cmds

caption = "**UPLOADED BY** Darmi"

@gez.on_message(filters.command("gasupan", "*") & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command("asupan", cmds) & filters.me)
async def asupan(client: Client, message: Message):
    if message.chat.id in BL_GCAST:
        return await edit_or_reply(message, "**Tidak bisa di gunakan di Group Support**")
    gz = await edit_or_reply(message, "`mencari asupan...`")
    await gather(
        gz.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "punyakenkan", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@gez.on_message(filters.command("gayang", "*") & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command("ayang", [".", "-", "^", "!", "?"]) & filters.me)
async def ayang(client, message):
    yanto = await message.reply("🔎 `Search Ayang...`")
    pop = message.from_user.first_name
    ah = message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "CeweLogoPack", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Ayangnya [{pop}](tg://user?id={ah}) 💝",
    )

    await yanto.delete()


@gez.on_message(filters.command("gppcp", "*") & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command("ppcp", [".", "-", "^", "!", "?"]) & filters.me)
async def ppcp(client, message):
    yanto = await message.reply("🔎 `Search PP Couple...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "ppcpcilik", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption="📌 PP Couple nya Nih Kak",
    )

    await yanto.delete()


@gez.on_message(filters.command("gppanime", "*") & filters.user(DEVS) & ~filters.me)
@gez.on_message(filters.command("ppanime", [".", "-", "^", "!", "?"]) & filters.me)
async def ppanime(client, message):
    yanto = await message.reply("🔎 `Search PP Anime...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "animehikarixa", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption="📌 PP Anime nya Nih Kak",
    )

    await yanto.delete()


add_command_help(
    "asupan",
    [
        [
            f"{cmds}asupan",
            f"{cmds}Asupan video TikTok",
        ],
        [f"{cmds}ayang", "Mencari Foto ayang kamu /nNote: Modul ini buat cwo yang jomblo."],
        [f"{cmds}ppcp", "Mencari Foto PP Couple Random."],
        [f"{cmds}ppanime", "Mencari Foto PP Couple Anime."],
    ],
)
