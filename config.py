# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "6119632")

API_HASH = os.environ.get("API_HASH", "5b51582f938e93c8eab32612d5045737")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6426072097:AAFpvNEzW65qVT6XwTxzafDLJKFk-Xtbun0") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renam")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://amal:amal@cluster0.6qbjqaa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "0"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1869495895').split()]

PORT = os.environ.get("PORT", "5656")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
