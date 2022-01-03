from yt_dlp import YoutubeDL

#logging-------------------------------------------------------------------------------------------

class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)
        
#----------------------------------------------------------------------------------------------------------

ydlp_opts={'logger': MyLogger(),
          'outtmpl': '%(title)s.%(ext)s',
          'no_warnings': True, 
          'progress_hooks': [my_hook],
          'quiet': True }


def ytdl(url):
    with yt_dlp.YoutubeDL(ydlp_opts) as ydl:
        ydl.download([url])
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None) 
        video_ext = info_dict.get('ext', None) 
        return video_title + '.' + video_ext
