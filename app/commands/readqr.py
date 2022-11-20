from telegram import Update
from telegram.ext import CallbackContext
#import qrcode
#from ..utils import log
#import os
#from PIL import Image
#from pyzbar.pyzbar import decode
from PIL import Image
import urllib.request

def readqr(update: Update, context: CallbackContext):
	#CAACAgEAAxkDAAIBHWN6nrsXQy_C7Mzb_DXSZ-Gu0A_8AAJ0AgAChgTZR2sxi5dGdFeXKwQ
	file = context.bot.getFile('CAACAgEAAxkDAAIBHWN6nrsXQy_C7Mzb_DXSZ-Gu0A_8AAJ0AgAChgTZR2sxi5dGdFeXKwQ')
	file_url = str(file.file_path)
	update.message.reply_text('path to file:' + file_url)
	urllib.request.urlretrieve(file_url, "qrsticker.webp")
	#update.message.reply_text('POLO')
	decocdeQR = decode(Image.open('qrsticker.webp'))
	response = decocdeQR[0].data.decode('ascii')
	update.message.reply_text(response)