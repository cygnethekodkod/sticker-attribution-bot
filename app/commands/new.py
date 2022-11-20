from telegram import Update
from telegram.ext import CallbackContext

from ..utils import log, user_states


def new(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    log.info(user_states)
    user_states[chat_id] = {}
    user_states[chat_id]['command'] = 'new'
    log.info(user_states)
    update.message.reply_text('new')
