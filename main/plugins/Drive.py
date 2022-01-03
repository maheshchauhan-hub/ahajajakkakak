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
from ethon.pyfunc import video_metadata, bash
from LOCAL.localisation import SUPPORT_LINK
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from telethon.tl.types import MessageMediaWebPage

def drive_folder_download(url):
    output = gdown.download_folder(url, quiet=True)
    return output

async def upload_folder(folder, event, edit):
    text = f'**UPLOADED by:** {BOT_UN}'
    index = len(folder)
    for i in range(int(index)):
        try:
            uploader = await fast_upload(f'{folder[i]}', f'{folder[i]}', time.time(), event.client, edit, f'**UPLOADING FILE - {int(i)}:**')
            await Drone.send_file(event.chat_id, uploader, caption=text, force_document=True)
            os.remove(folder[i])
        except Exception as e:
            print(e)
            return await edit.edit(f"An error [`{e}`] occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
    
    
async def compress(event, msg):
    cmd = ""
    Drone = event.client
    edit = await Drone.send_message(event.chat_id, "Trying to process.", reply_to=msg.id)
    link = msg.media.webpage.url
    if 'folder' in link:
        try:
            folder = drive_folder_download(link)
        except Exception as e:
            print(e)
            return await edit.edit(f"An error [`{e}`] occured while Downloading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
        await upload_folder(folder, event, edit) 
    elif 'folders' in link:
        try:
            folder = drive_folder_download(link)
        except Exception as e:
            print(e)
            return await edit.edit(f"An error [`{e}`] occured while Downloading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
        await upload_folder(folder, event, edit) 
    elif 'https://drive.google.com/file/' in link:
        id = (link.split("/"))[5]
        _link = f'https://drive.google.com/uc?id={id}'
        try:
            file = gdown.download(_link, quiet=True)
            try:
                uploader = await fast_upload(f'{file}', f'{file}', time.time(), event.client, edit, f'**UPLOADING FILE:**')
                await Drone.send_file(event.chat_id, uploader, caption=text, force_document=True)
            except Exception as e:
                print(e)
                return await edit.edit(f"An error [`{e}`] occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
        except Exception as e:
            print(e)
            return await edit.edit(f"An error [`{e}`] occured while Downloading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
        os.remove('file')
    elif 'https://drive.google.com/uc?id=' in link:
        try:
            file = gdown.download(link, quiet=True)
            try:
                uploader = await fast_upload(f'{file}', f'{file}', time.time(), event.client, edit, f'**UPLOADING FILE:**')
                await Drone.send_file(event.chat_id, uploader, caption=text, force_document=True)
            except Exception as e:
                print(e)
                return await edit.edit(f"An error [`{e}`] occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
        except Exception as e:
            print(e)
            return await edit.edit(f"An error [`{e}`] occured while Downloading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
        os.remove('file')
        
        
        
        
        
        
    
