import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message


async def echo(message: Message):
    await message.answer(message.text)


async def on_startup(dp):
    print('Бот запущен')


bot = Bot(token='')
dp = Dispatcher()


async def main():
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())