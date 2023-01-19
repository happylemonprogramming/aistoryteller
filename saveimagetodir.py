import requests
from PIL import Image

def saveimagetodir(url,path,name):
    # Locating image on web
    img = Image.open(requests.get(url, stream = True).raw)
    # Saving file on server
    img.save(f'{path}/{name}.png')
    # File path and name
    file = f'{path}/{name}.png'
    return url, file