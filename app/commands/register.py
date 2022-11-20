from telegram import Update
from telegram.ext import CallbackContext

from ..utils import log

def register(update: Update, context: CallbackContext):
  f = open('app/test.png', 'rb')
  shortname =  update.message.from_user.username + '_by_StickerAttributionBot'
  log.info(shortname)
  # stickerset = context.bot.create_new_sticker_set(update.message.from_user.id, shortname, 'Test', png_sticker=f, emojis='🤖')
  # stickerset = context.bot.get_sticker_set(shortname)
  log.info(stickerset)
  # file = context.bot.upload_sticker_file(update.message.from_user.id, f)
  # log.info(file)
  # file_id = file.file_id
  # unique_id = file.file_unique_id
  # context.bot.sendSticker(chat_id=update.message.chat_id,sticker=file_id)
  # update.message.reply_sticker(file_id)
  # update.message.reply_sticker('CAACAgQAAxkBAAPDY3BQk_YQJfawbNuyIrxRIP_2dMUAAlUNAAIBfYlTeSUW4bHoIp8rBA')
  update.message.reply_sticker(stickerset.stickers[0].file_id)
  # update.message.reply_markdown(stickerset.stickers[0].file_id)