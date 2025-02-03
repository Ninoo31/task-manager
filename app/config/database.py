import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv

load_dotenv()

  # Remplace par une variable d'environnement pour plus de flexibilité

engine = create_engine(os.getenv("DATABASE_URL", "sqlite:///tasks.db"), connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
class Base(DeclarativeBase):
    pass

def init_db():
    """Initialise la base de données en créant les tables si elles n'existent pas."""
    from app.models.User import User
    from app.models.Task import Task
    Base.metadata.create_all(bind=engine)