#For youtubedownload------------------------------------------------------------------------------------------------

from youtube_dl import YoutubeDL 

async def youtube(url):
    options = {
        "geo-bypass": True,
        "nocheckcertificate": True,
        "outtmpl": "%(title)s.%(ext)s",
        "format": "best",
        "quiet": True }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None) 
        video_ext = info_dict.get('ext', None) 
        return video_title + '.' + video_ext
    
    
