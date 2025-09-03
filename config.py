import os
from dotenv import load_dotenv

load_dotenv()

# Box Config
BOX_CLIENT_ID = os.getenv("BOX_CLIENT_ID")
BOX_CLIENT_SECRET = os.getenv("BOX_CLIENT_SECRET")
BOX_ACCESS_TOKEN = os.getenv("BOX_ACCESS_TOKEN")

# Interlinked Config
INTERLINKED_API_KEY = os.getenv("INTERLINKED_API_KEY")

# Validation
if not BOX_CLIENT_ID or not BOX_CLIENT_SECRET or not BOX_ACCESS_TOKEN:
    raise ValueError("❌ Missing Box API credentials in .env")

if not INTERLINKED_API_KEY:
    raise ValueError("❌ Missing Interlinked API key in .env")
