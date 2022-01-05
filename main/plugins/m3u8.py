

"""NOT IN USE"""

import m3u8
import requests
import datetime
import os
from Crypto.Cipher import AES
from Crypto import Random
from datetime import datetime as dt
import glob
# Request header, not necessary, see website change
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

def download(ts_urls, download_path):
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    for i in range(len(ts_urls)):
        ts_url = ts_urls[i]
        file_name = ts_url.uri
        start = datetime.datetime.now().replace(microsecond=0)
        response = requests.get(file_name, allow_redirects=True)
        ts_path = download_path+"/{0}.ts".format(i)
        with open(ts_path,"wb+") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

        end = datetime.datetime.now().replace(microsecond=0)
        print("total time: %s"%(end-start))

def merge_to_mp4(dest_file, source_path, delete=True):
    with open(dest_file, 'wb') as fw:
        files = glob.glob(source_path + '/*.ts')
        for file in files:
            with open(file, 'rb') as fr:
                fw.write(fr.read())
            if delete:
                os.remove(file)
       
def download_m3u8_video(url, path):                
    video = m3u8.load(url)
    segments = []
    segments.append(video.segments)
    download(segments, 'tmp')
    merge_to_mp4(path, 'tmp')
    
"""NOT IN USE"""
