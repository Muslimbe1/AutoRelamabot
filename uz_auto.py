from aiogram import Bot, Dispatcher, executor, types
import logging
from uz_api_token import API_TOKEN1
from add_user import add_user
from qnopka import restart, inline_markup, cars, damas_colors

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN1)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def do_start(message: types.Message):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    try:
        add_user(tg_id=user_id, full_name=full_name, username=username)
        await message.answer(f"Assalomu aleykum {full_name}!\nSiz asosiy menyudasiz", reply_markup=restart)
        await message.answer('"UzAuto" botga xush kelibsiz, kerakli bo\'limni tanlang', reply_markup=inline_markup)
    except Exception as error:
        logging.error(error)


@dp.callback_query_handler(text="back")
async def do_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('"UzAuto" botga xush kelibsiz, kerakli bo\'limni tanlang', reply_markup=inline_markup)


@dp.callback_query_handler(text="price")
async def get_price(call: types.CallbackQuery):
    await call.message.edit_text("Pastdagi ro'yxatdan mashinani tanlang ", reply_markup=cars)


@dp.callback_query_handler(lambda call: call.data in ["Damas", "white"])
async def get_damas_info(call: types.CallbackQuery):
    # photo3="https://lionmotors.uz/wp-content/uploads/2020/11/damaswhite.jpg"
           await call.message.delete()
    await call.message.answer_photo(photo="https://lionmotors.uz/wp-content/uploads/2020/11/damaswhite.jpg", caption="🕹 Позиция: D2 STYLE\n💵 Нарх: 86,971,000 сўм\n🛢 100 км га сарфи: 7,8 л/100 км\n🐎 Қуввати: 38 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 5 МT\n🎨 Ранги: Summit White", reply_markup=damas_colors)
    # await call.message.edit_media(media=types.InputMediaPhoto(media=photo3,caption="🕹 Позиция: D2 STYLE\n💵 Нарх: 86,971,000 сўм\n🛢 100 км га сарфи: 7,8 л/100 км\n🐎 Қуввати: 38 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 5 МT\n🎨 Ранги: Summit White"), reply_markup=damas_colors)


@dp.callback_query_handler(text="gray")
async def get_gray_info(call: types.CallbackQuery):
    photo2="https://frankfurt.apollo.olxcdn.com/v1/files/0mskljuawc5u-UZ/image"
    # await call.message.delete()
    # await call.message.answer_photo(photo="https://frankfurt.apollo.olxcdn.com/v1/files/0mskljuawc5u-UZ/image", caption="🕹 Позиция: D2 STYLE \n💵 Нарх: 86,971,000.000 сўм\n🛢 100 км га сарфи: 7,8 л/100 км\n🐎 Қуввати: 38 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 5 МT\n🎨 Ранги: Artemis Gray", reply_markup=damas_colors)
    await call.message.edit_media(media=types.InputMediaPhoto(media=photo2, caption="🕹 Позиция: D2 STYLE \n💵 Нарх: 86,971,000.000 сўм\n🛢 100 км га сарфи: 7,8 л/100 км\n🐎 Қуввати: 38 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 5 МT\n🎨 Ранги: Artemis Gray"), reply_markup=damas_colors)

@dp.callback_query_handler(text="blue")
async def get_gray_info(call: types.CallbackQuery):
    photo1="https://avtotexxizmat.uz/uploads/car-color/KK/KK/Kf/1635146513.png"
    # await call.message.delete()
    # await call.message.answer_photo(photo="https://avtotexxizmat.uz/uploads/car-color/KK/KK/Kf/1635146513.png", caption="🕹 Позиция: D2 STYLE\n💵 Нарх: 86,971,000.000 сўм\n🛢 100 км га сарфи: 7,8 л/100 км\n🐎 Қуввати: 38 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 5 МT\nРанги: Blue", reply_markup=damas_colors)
    await call.message.edit_media(media=types.InputMediaPhoto(media=photo1, caption="🕹 Позиция: D2 STYLE\n💵 Нарх: 86,971,000.000 сўм\n🛢 100 км га сарфи: 7,8 л/100 км\n🐎 Қуввати: 38 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 5 МT\nРанги: Blue"),reply_markup=damas_colors)


@dp.callback_query_handler(text="beige")
async def get_beige_info(call: types.CallbackQuery):
    photo = "https://lionmotors.uz/wp-content/uploads/2020/11/damas2.jpg"
    # await call.message.delete()
    await call.message.edit_media(media=types.InputMediaPhoto(media=photo, caption="🕹 Позиция: D2 STYLE\n💵 Нарх: 86,971,000.000 сўм\n🛢 100 км га сарфи: 7,8 л/100 км\n🐎 Қуввати: 38 л.с. при 5000 об/мин\n⚙️ Трансмиссия: 5 МT\n🎨 Ранги: Smoke Beige"), reply_markup=damas_colors)
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
