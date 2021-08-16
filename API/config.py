import os
from dotenv import load_dotenv

load_dotenv()
PORT = os.getenv("PORT")
MONGO_URL = os.getenv("MONGO_URL")

