import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'api'))

from api.database import Base, engine
from api import models

def init_db():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_db() 