#ChauhanMahesh/DroneBots/COL

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = int(4796990)
API_HASH = "32b6f41a4bf740efed2d4ce911f145c7"
BOT_TOKEN = "5089347286:AAEmf4L1IWrDMsOVpWcr7XI8ZE6F4LB_05s"
BOT_UN = "@TheUploaderProBot"
AUTH_USERS = int(1295012425)
LOG_CHANNEL = "VcBotLog"
LOG_ID = int(-1001180718837)
FORCESUB = int(-1001485129059)
FORCESUB_UN = "DroneBots"
ACCESS_CHANNEL = int(-1001683603362)
MONGODB_URI = "mongodb+srv://Vasusen:darkmaahi@cluster0.o7uqb.mongodb.net/cluster0?retryWrites=true&w=majority"
    
Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
