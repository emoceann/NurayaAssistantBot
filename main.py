from aiogram.utils import executor
from create_Bot import dp

async def on_startup(_):
    print('Bot online')



from handlers import wordsimage, texttowritten

wordsimage.register_handlers_admin(dp)
texttowritten.register_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)