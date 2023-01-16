import requests
from PIL import Image

def saveimagetodir(url,path,name):
    # url = 'https://hyperlink.com'
    img = Image.open(requests.get(url, stream = True).raw)
    # img.save(str(path)+str(name)+'.png')
    img.save(f'{path}\{name}.png')
    # file = str(path)+str(name)+'.png'
    file = f'{path}\{name}.png'
    return url, file