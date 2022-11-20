from .db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  telegram_id = db.Column(db.BigInteger)
  qr_id = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
  sticker_packs = db.relationship('StickerPack', backref='user', lazy=True)
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

class StickerPack(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  short_name = db.Column(db.String(64))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  stickers = db.relationship('Sticker', backref='sticker_pack', lazy=True)
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

attribution_links = db.Table('attribution_links',
  db.Column('sticker_id', db.Integer, db.ForeignKey('sticker.id'), primary_key=True),
  db.Column('attribution_id', db.Integer, db.ForeignKey('attribution.id'), primary_key=True)
)

class Sticker(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  file_id = db.Column(db.String(64))
  file_unique_id = db.Column(db.String(32))
  pack_id = db.Column(db.Integer, db.ForeignKey('sticker_pack.id'), nullable=False)
  attributions = db.relationship('Attribution', secondary=attribution_links, lazy='subquery',
        backref=db.backref('sticker', lazy=True))
  created_at = db.Column(db.DateTime, server_default=db.func.now())
  updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

class Attribution(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64))
  link = db.Column(db.String(255))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  label_id = db.Column(db.Integer, db.ForeignKey('attribution_label.id'), nullable=False)

class AttributionLabel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  label = db.Column(db.String(64))

