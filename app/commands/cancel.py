from telegram import Update
from telegram.ext import CallbackContext
from ..utils import user_states

def cancel(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    value = user_states.pop(chat_id, {"command": "none"}) 
    update.message.reply_text('Canceled the command to ' + value['command'])
