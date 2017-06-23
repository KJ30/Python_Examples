import requests
import os
import shutil

# Connects to URL and Saves images to folder

def get_cat(folder, name):
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'
    data = get_data_from_url(url)
    save_image(folder, name, data)


# connects to URL

def get_data_from_url(url):
    response = requests.get(url, stream=True)
    return response.raw

# Saves Images to file path

def save_image(folder, name, data):
    file_name = os.path.join(folder, name + '.jpg')
    with open(file_name, 'wb') as fout:
        shutil.copyfileobj(data, fout)
