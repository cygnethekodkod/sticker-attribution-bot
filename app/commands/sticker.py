from telegram import Update
from telegram.ext import CallbackContext
from ..models import Sticker

from .help_command import format_help_command

from ..utils import log

def sticker(update: Update, context: CallbackContext):
  chat_id = update.message.chat.id
  text = update.message.text
  sticker = update.message.sticker
  user_id = update.message.chat.id
  log.info(sticker)
  # stickerset = context.bot.getStickerSet(sticker.set_name)
  # log.info(stickerset)
  file = context.bot.getFile(sticker.file_id)
  sticker_entity = Sticker.query.filter_by(file_unique_id=file.file_unique_id).first()
  if (sticker_entity is None):
    log.info('Nothing to see here!')
    update.message.reply_markdown('No info found!')
    return
  log.info(file)
  log.info(sticker_entity)
  # context.bot.addStickerToSet(user_id=user_id, name='Cygne', png_sticker=sticker.file_id, emojis="😊")

    # open the image
  image = Image.open(file.file_path)

  log.info(image)

  
  reply = sticker.file_unique_id
  reply += '\n\n'
  reply += sticker.file_id

  update.message.reply_markdown(
    reply,
    quote=False,
  )
