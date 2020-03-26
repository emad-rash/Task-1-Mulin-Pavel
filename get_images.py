import requests
import shutil
import base64
import json





def find_image():
    #set stream to True, this will return the stream content.
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    if url.split('.')[2] == 'jpg':
        print('there is')
        print(url)
        image = requests.get(url, stream=True)
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        image.raw.decode_content = True
    else:
        image = 0
    return image


def save_image(number):
    image = find_image()
    if image != 0:
        file = open('images/dog_'+str(number)+'.jpg', 'wb')
        # Copy the response stream raw data to local image file.
        shutil.copyfileobj(image.raw, file)
    else:
        save_image(number)



for i in range(51,76):
    save_image(i)
