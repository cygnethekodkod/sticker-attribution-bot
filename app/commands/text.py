from telegram import Update
from telegram.ext import CallbackContext

from ..utils import user_states

def text(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id
    current_command = "none"
    update.message.reply_text('Your current command is ' + current_comand)
