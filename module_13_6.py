from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


kb1 = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories")
button4 = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
kb1.add(button3)
kb1.add(button4)

menu_start = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Рассчитать"),
        KeyboardButton(text="Информация")
    ]],
    resize_keyboard=True)


# button1 = KeyboardButton(text="Рассчитать")
# button2 = KeyboardButton(text="Информация")
# kb.add(button1)
# kb.add(button2)

@dp.message_handler(commands=['start'])
async def main_menu(message):
    await message.answer("Привет, я бот, помогающий с твои здоровьем", reply_markup=menu_start)


@dp.message_handler(text="Рассчитать")
async def starter(message):
    await message.answer("выбери опцию", reply_markup=kb1)


@dp.callback_query_handler(text="calories")
async def infor1(call):
    await call.message.answer("Введите свой возраст:")
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def sset_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calorii = 10 * int(data['weight']) + 6.25 * int(data['growth']) + 5 * int(data['age']) + 5
    await message.answer(f"Наш ответ по калориям {calorii}")
    await state.finish()


@dp.callback_query_handler(text="formulas")
async def infor2(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
