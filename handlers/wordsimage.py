from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from create_Bot import dp, bot
from pytesseract import pytesseract
import cv2

pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class FSM_Admin(StatesGroup):
    picture = State()

async def imagetotext(message: types.Message):
    await FSM_Admin.picture.set()
    await message.reply('Upload picture')

async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['picture'] = message.photo[0].file_id
        await message.photo[-1].download('wordimg/test.jpg')
        img = cv2.imread('wordimg/test.jpg')
        words = pytesseract.image_to_string(img, lang='rus+eng')
    await message.reply(words)
    await state.finish()



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(imagetotext, commands='wordimg', state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSM_Admin.picture)

