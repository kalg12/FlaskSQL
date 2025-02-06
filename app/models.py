import uuid
from app import db

class Kevin(db.Model):
    __tablename__ = 'kevin'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(100), nullable=False, index=True)
    apellidos = db.Column(db.String(100), nullable=False, index=True)
    telefono = db.Column(db.String(20), nullable=False, index=True)

    def __repr__(self):
        return f'<Kevin {self.nombre} {self.apellidos}>'