from telegram import Bot
from telegram.ext import (CallbackQueryHandler, CommandHandler, Dispatcher,
                          Filters, MessageHandler)

from config import BOT_TOKEN

from .commands import (callback_query, cancel, error, help_command, new, polo, register, start, sticker,
                       text, unknown, version, qtsticks, readqr)
from .utils import log
#from qrcode import make

def create_dispatcher():
  try:
    bot = Bot(BOT_TOKEN)
    dispatcher = Dispatcher(bot, None, workers=1)

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler(['h', 'help'], help_command))
    dispatcher.add_handler(CommandHandler('marco', polo))
    dispatcher.add_handler(CommandHandler('new', new))
    dispatcher.add_handler(CommandHandler('cancel', cancel))
    dispatcher.add_handler(CommandHandler('register', register))
    dispatcher.add_handler(CommandHandler(['v', 'ver', 'version'], version))
    dispatcher.add_handler(CommandHandler('qr', qtsticks))
    dispatcher.add_handler(CommandHandler('readqr', readqr))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))
    dispatcher.add_handler(MessageHandler(Filters.sticker, sticker))
    dispatcher.add_handler(MessageHandler(Filters.text, text))
    dispatcher.add_handler(CallbackQueryHandler(callback_query))
    dispatcher.add_error_handler(error)

    log.info('Initializing bot... %s', 'OK')

    return dispatcher
  except Exception as exc:
    log.exception('Initializing bot... %s: %s', 'ERR', exc)

    return None

dispatcher = create_dispatcher()
