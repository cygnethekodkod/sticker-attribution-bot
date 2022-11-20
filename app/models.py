from .db import db
from sqlalchemy.dialects.postgresql import UUID

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  telegram_id = db.Column(db.BigInteger)
  qr_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
  sticker_packs = db.relationship('StickerPack', backref='user', lazy=True)
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

  def __init__(self, telegram_id):
    self.telegram_id = telegram_id

class StickerPack(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  short_name = db.Column(String(64))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  stickers = db.relationship('Sticker', backref='sticker_pack', lazy=True)
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

  def __init__(self, short_name, user_id):
    self.short_name = short_name
    self.user_id = user_id

attribution_links = db.Table('attribution_links',
  db.Column('sticker_id', db.Integer, db.ForeignKey('sticker.id'), primary_key=True),
  db.Column('attribution_id', db.Integer, db.ForeignKey('attribution.id'), primary_key=True)
)

class Sticker(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  file_id = db.Column(String(64))
  file_unique_id = db.Column(String(32))
  pack_id = db.Column(db.Integer, db.ForeignKey('sticker_pack.id'), nullable=False)
  attributions = db.relationship('Attribution', secondary=attribution_links, lazy='subquery',
        backref=db.backref('sticker', lazy=True))
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

  def __init__(self, file_id, file_unique_id, pack_id):
    self.file_id = file_id
    self.file_unique_id = file_unique_id
    self.pack_id = pack_id

class Attribution(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(String(64))
  link = db.Column(String(255))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  label_id = db.Column(db.Integer, db.ForeignKey('attribution_label.id'), nullable=False)

class AttributionLabel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  label = db.Column(String(64))

  def __init__(self, label): 
    self.label = label
