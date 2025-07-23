import os
from dotenv import load_dotenv

load_dotenv()   # reads .env into os.environ

class Config:
    DATABASE    = os.getenv("DATABASE_PATH", "users.db")
    SECRET_KEY  = os.getenv("SECRET_KEY",  "change_me_in_prod")
