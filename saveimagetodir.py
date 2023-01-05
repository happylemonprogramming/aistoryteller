import requests
from PIL import Image
from pathlib import Path

def saveimagetodir(url,path,name):
    # url = 'https://hyperlink.com'
    img = Image.open(requests.get(url, stream = True).raw)
    img.save(str(path)+str(name)+'.png')
    return url