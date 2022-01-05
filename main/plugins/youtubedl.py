from pyUltroid.functions.ytdl import download_yt

#For youtube videos download
def youtube(url, event):
    options = {
        "nocheckcertificate": True,
        "geo-bypass": True,
        "outtmpl": "%(id)s.mp4",
        "format": "best",
        "quiet": True }
    options["postprocessors"] = [{"key": "FFmpegMetadata"}]
    await download_yt(edit, url, options) 
    
