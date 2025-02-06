import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://u223049366_sitemasquinto:/4dU0mFKn1B@srv1838.hstgr.io/u223049366_sitemasquinto"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)

    # 🔹 Ajustes para mantener la conexión estable
    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_recycle": 280,   # Reinicia conexiones inactivas
        "pool_size": 10,       # Número máximo de conexiones activas
        "max_overflow": 20,    # Conexiones adicionales permitidas
        "pool_pre_ping": True, # Verifica si la conexión sigue activa
    }