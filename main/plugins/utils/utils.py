from main import BOT_UN
from telethon import events
from ethon.telefunc import fast_upload

video_mimes = ['mp4',
               'mkv', 
               'webm']
               
#uploads a folder 
#Note:Here folder is a list of all contents in a folder
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
    
