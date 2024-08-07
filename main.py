import asyncio
import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command('photo'))
async def photo_handler(message: Message):
    photos = [
        'https://wap.spartakfanat.ru/gallery/logo/Emblema_FC_Spartak_2013.png',
        'https://cdn1.ozone.ru/s3/multimedia-5/c600/6131037341.jpg',
        'https://home.sportb2b.ru/media/User/CompanyCustomer/2022-12-05/e466707094a6fb9b3253017fb5641b5c.jpg'
    ]
    rand_photo = random.choice(photos)
    await message.answer_photo(photo=rand_photo, caption='Спартак ЧЕМПИОН')


@dp.message(F.text == 'Спартак')
async def aitext_handler(message: Message):
    await message.answer('ЧЕМПИОН')


@dp.message(F.photo)
async def react_photo_handler(message: Message):
    reactions = [
        'Ого, какая фотка!',
        'Непонятно, что это такое',
        'Не отправляйте пожалуйста такое больше'
    ]
    rand_reaction = random.choice(reactions)
    await message.answer(rand_reaction)


@dp.message(Command('help'))
async def help_handler(message: Message):
    await message.answer('Тут будет помощь \n/start \n/help')


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}!')


@dp.message()
async def echo_handler(message: Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())