from telegram import Update
from telegram.ext import CallbackContext
import qrcode
from ..utils import log
import os
from PIL import Image

def qtsticks(update: Update, context: CallbackContext):
  
  img = qrcode.make('fb1773ed-c715-47d0-a7ce-5bdd2cfbe520') #create QR code that includes specified data
  newsize = 128,128
  img.thumbnail(newsize, Image.Resampling.LANCZOS) #resize image to be 1/4 sticker size - resize method doesn't work
  img.save('test.png', format="png") #save the QR code to local to remove pillow formatting
  background = Image.open('app/background.png') #open template
  foreground = Image.open('test.png') #open qrcode
  background.paste(foreground, (0, 384)) #paste QR code onto background image
  background.save('test.webp', format="webp") #save combined image to local to remove pillow formatting
  f = open('./test.webp', 'rb') #open file as async datastream
  sticker_message = context.bot.sendSticker(chat_id=update.message.chat_id,sticker=f) #send sticker direct from generated file
  sticker_file_id = sticker_message.sticker.file_id #store sticker file_id for later reuse
  update.message.reply_text('sticker filed_id is:' + str(sticker_file_id))
  os.remove('test.png') #remove local copy of QR code
  os.remove('./test.webp') #remove local copy of generated sticker file
  


  #update.message.reply_text('sticker file_id is '+str(sticker_message.message_id))
  #update.message.reply_text('sticker file_id is '+str(sticker_message.sticker.file_id))
  #update.message.reply_text('sending sticker via file_id:')
  #context.bot.sendSticker(chat_id=update.message.chat_id,sticker=sticker_message.sticker.file_id)
  
  #Ignore the below

  """
  img = qrcode.make('test my best') #create QR code that includes specified data
  img.save('test.webp', format="webp") #save the QR code to local to remove pillow formatting
  f = open('./test.webp', 'rb') #open file as datastream
  #webfile = context.bot.upload_document(update.message.from_user.id, f)
  #file = context.bot.upload_sticker_file(update.message.from_user.id, f) #upload file as sticker to telegram server
  #webfile_id = webfile.id
  #file_id = file.file_id #get id from uploaded file
  #context.bot.sendDocument
  context.bot.sendSticker(chat_id=update.message.chat_id,sticker=f)
  #context.bot.sendDocument(chat_id=update.message.chat_id,document=webfile_id)
  #update.message.reply_text('jrl')
  os.remove('./test.webp')
  update.message.reply_text('but why')
  """
  #---
  """
  qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=8,
    border=4,
  )
  qr.add_data('i tell you hwat')
  qr.make
  img = qr.make_image()
  newsize = (512,512)
  img.save('test.webp', format="webp")
  f = open('./test.webp', 'rb')
  #file = context.bot.upload_sticker_file(update.message.from_user.id, f)
  #file_id = file.file_id #get id from uploaded file
  context.bot.sendSticker(chat_id=update.message.chat_id,sticker=f)
  os.remove('./test.webp')
  update.message.reply_text('but why')
  """

  """
  update.message.reply_text(str(os.getcwd()))
  parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
  img.resize(newsize)
  update.message.reply_text('qrcode size is:'+str(img.size[0])+'x'+str(img.size[1]))
  img.save('test.webp', format="webp") #save the QR code to local to remove pillow 
  """