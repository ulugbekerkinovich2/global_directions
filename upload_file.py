import requests
import os
from icecream import ic
from add_university import token
import json
import time
from tqdm import tqdm
origin = 'https://admin.iapply.org'

ic(token)

def uploadfile(token, associated_with, usage, file_name):
    url = "https://api.iapply.org/v1/images/upload"
    headers = {
        'Authorization': f'Bearer {token}',
        'Origin': origin
    }
    files = {
        'file': (os.path.basename(file_name), open(file_name, 'rb'), 'image/png'),
        'associated_with': (None, associated_with),
        'usage': (None, usage)
    }

    response = requests.post(url, headers=headers, files=files)
    data = response.json()
    return data['path']

# res = uploadfile(token, 'university', 'logo', '/Users/jurakulovamadinabonu/python_projects/global_directions/images_logo/Abertay University.jpg')  # Corrected usage value to 
# data = res.json()
# ic(res)

with open("universities_images.json", 'r', encoding='utf8') as f:
    data_uni_images = json.load(f)
array_ig = []
for obj in tqdm(data_uni_images):
    university_name = obj["university_name"],
    profile_image = obj["profile_image"]
    res = uploadfile(token, 
                    'university',
                    'logo', 
                    f'/Users/jurakulovamadinabonu/python_projects/global_directions/images_logo/{profile_image}'
            )
    new_obj = {
        'university_name': university_name,
        'path': res
    }
    time.sleep(0.2)
    array_ig.append(new_obj)
    with open('uploaded_images.json', 'w', encoding='utf8') as f:
        json.dump(array_ig, f, ensure_ascii=False)
    