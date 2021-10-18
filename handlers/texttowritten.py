from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_Bot import dp, bot
from pywhatkit import text_to_handwriting


class FSM_Admin(StatesGroup):
    text = State()


async def text_state(message: types.Message):
    await FSM_Admin.text.set()
    await message.reply('Write your text')

async def text_handwritten_state(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    handwritten = text_to_handwriting(message.text, save_to='texthand/test.png')
    await bot.send_photo(user_id, photo=open('texthand/test.png', 'rb'))
    await state.finish()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(text_state, commands='txttohw', state=None)
    dp.register_message_handler(text_handwritten_state, state=FSM_Admin.text)