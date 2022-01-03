import time
from main.__int__ import BOT_UN
from telethon import events
from ethon.telefunc import fast_upload
from telethon.tl.types import DocumentAttributeVideo
from ethon.pyutils import file_extension

video_mimes = ['mp4',
               'mkv', 
               'webm']

#attrubutes needed to upload video as streaming
def attributes(file):
    metadata = video_metadata(file)
    width = metadata["width"]
    height = metadata["height"]
    duration = metadata["duration"]
    x = [DocumentAttributeVideo(duration=duration, w=width, h=height, supports_streaming=True)]
    return x

#uploads video in streaming form
async def upload_video(file, event, edit):
    try:
        x = attributes(file)
        uploader = await fast_upload(file, file, time.time(), event.client, edit, f'**UPLOADING FILE**')
        await Drone.send_file(event.chat_id, uploader, caption=text, attributes=x, force_document=False)
        os.remove(file)
    except Exception:
        False    

    
#uploads a folder 
#Note:Here folder is a list of all contents in a folder
async def upload_folder(folder, event, edit):
    text = f'**UPLOADED by:** {BOT_UN}'
    index = len(folder)
    for i in range(int(index)):
        try:
            if folder[i] in video_mimes:
                result = await upload_video(folder[i], event, edit) 
                if result is False:
                  
            uploader = await fast_upload(f'{folder[i]}', f'{folder[i]}', time.time(), event.client, edit, f'**UPLOADING FILE:**')
            await Drone.send_file(event.chat_id, uploader, caption=text, force_document=True)
            os.remove(folder[i])
        except Exception as e:
            print(e)
            return await edit.edit(f"An error [`{e}`] occured while uploading.\n\nContact [SUPPORT]({SUPPORT_LINK})", link_preview=False)
    
