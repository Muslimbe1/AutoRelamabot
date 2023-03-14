from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

restart = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton(text="🔃 Ботни қайта ишга тушириш")]])

inline_markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Avtomobil narxlari", callback_data="price")],
    [InlineKeyboardButton(text="Sotuvda borligi to'g'risda malumot", callback_data="sell_data")],
    [InlineKeyboardButton(text="So'nggi yangiliklar", callback_data="latest_news")],
    [InlineKeyboardButton(text="Avtomobillar informatsiyasi", callback_data="auto_info")]
])

gm_cars = ["Damas", "Cobalt (124,295,000so'm dan)", "Malibu 2 (394,900,000 so'm dan)", "Gentra (128,248,000 so'm dan)",
           "Onix (152,996,000 so'm dan)", "Tracker 2 (211,454,880 so'm dan)", "Equinox (389,000,000 so'm dan)"]
cars = InlineKeyboardMarkup(row_width=1)
back_button = InlineKeyboardButton(text="Orqaga", callback_data="back")
for car in gm_cars:
    cars.insert(InlineKeyboardButton(text=car, callback_data=car))

cars.row(back_button)

damas_colors = InlineKeyboardMarkup()
damas_colors.row(InlineKeyboardButton(text="Summit white", callback_data="white"))
damas_colors.row(InlineKeyboardButton(text="Artemis gray", callback_data="gray"))
damas_colors.row(InlineKeyboardButton(text="Blue", callback_data="blue"))
damas_colors.row(InlineKeyboardButton(text="Smoke beige", callback_data="beige"))
damas_colors.row(back_button)
