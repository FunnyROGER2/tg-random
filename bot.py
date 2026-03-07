"""
Telegram-бот для случайного выбора пользователя из группы.
Команды: /random, /randomothers (исключая отправителя).
"""
import asyncio
import os
import random
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]

app = Client(
    "tg_random_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)


def is_real_user(member) -> bool:
    """Проверяет, что участник — реальный пользователь, а не бот."""
    return not getattr(member.user, "is_bot", True)


async def get_eligible_members(chat_id: int, exclude_user_id: int | None = None) -> list:
    """
    Собирает список реальных пользователей группы.
    exclude_user_id — ID пользователя, которого исключить (для /randomothers).
    """
    members = []
    async for member in app.get_chat_members(chat_id):
        if not is_real_user(member):
            continue
        if exclude_user_id is not None and member.user.id == exclude_user_id:
            continue
        members.append(member)
    return members


@app.on_message(filters.command("random") & filters.group)
async def cmd_random(client: Client, message: Message):
    """Выбирает случайного пользователя из группы."""
    await handle_random(message, exclude_sender=False)


@app.on_message(filters.command("randomothers") & filters.group)
async def cmd_random_others(client: Client, message: Message):
    """Выбирает случайного пользователя из группы, исключая отправителя."""
    await handle_random(message, exclude_sender=True)


async def handle_random(message: Message, *, exclude_sender: bool):
    chat_id = message.chat.id
    sender_id = message.from_user.id if message.from_user else None

    status_msg = await message.reply_text("Выбираем...")
    await asyncio.sleep(1)

    await status_msg.edit_text("🎲")
    await asyncio.sleep(1)

    members = await get_eligible_members(
        chat_id,
        exclude_user_id=sender_id if exclude_sender else None,
    )

    if not members:
        await status_msg.edit_text(
            "Не найдено подходящих участников. Добавьте бота в группу и убедитесь, "
            "что в ней есть реальные пользователи."
        )
        return

    chosen = random.choice(members)
    name = chosen.user.first_name or "Пользователь"
    mention = f"[{name}](tg://user?id={chosen.user.id})"
    await status_msg.edit_text(f"Ты доброволец! {mention}", parse_mode="Markdown")


def main():
    app.run()


if __name__ == "__main__":
    main()
