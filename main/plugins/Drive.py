#TG:ChauhanMahesh/DroneBots
#Github.com/vasusen-code

import re
import os
import time
import gdown
import asyncio
import subprocess
from datetime import datetime as dt
from .. import Drone, BOT_UN
from telethon import events
from ethon.telefunc import fast_download, fast_upload
from ethon.pyfunc import video_metadata
from LOCAL.localisation import SUPPORT_LINK
from LOCAL.utils import subprocess_progress
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from telethon.tl.types import MessageMediaWebPage

async def compress(event, msg):
    cmd = ""
    Drone = event.client
    edit = await Drone.send_message(event.chat_id, "Trying to process.", reply_to=msg.id)
    link = msg.media.webpage.url
    output = dt.now().isoformat("_", "seconds") + '.tar.gz'
    if 'https://drive.google.com/uc?id=' in link:
        cmd = f'gdown {link} -o {output}'
    elif 'https://drive.google.com/drive/folders/' in link:
        cmd = f'gdown {link} -o ./Drive/{event.senderid} --folder'
    elif 'https://drive.google.com/file/' in link:
        x = link.split("/")[5]
        _link = f'https://drive.google.com/uc?id={x}'
        cmd = f'gdown {_link} -o {output}'
    try:
        FT = time.time()
        progress = f"progress-{FT}.txt"
        await subprocess_progress(cmd, progress, FT, edit, '**DOWNLOADING:**')
    except Exception as e:
        print(e)
        return await edit.edit(f"An error [`{e}`] occured while Downloading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)  
    
        


