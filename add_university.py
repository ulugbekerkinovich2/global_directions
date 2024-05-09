import requests
import json
from icecream import ic
import os
import time
from tqdm import tqdm
import random
import string
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZmlyc3RfbmFtZSI6IlNoYWtoem9kIiwibGFzdF9uYW1lIjoiWW92a29jaGV2IiwicGhvbmUiOiIrOTk4OTc3MzQ4NDAxIiwiZW1haWwiOiJzeW92a29jaGV2QGdtYWlsLmNvbSIsImF2YXRhciI6bnVsbCwicm9sZSI6InN1cGVyX2FkbWluIiwiaXNfdmVyaWZ5Ijp0cnVlLCJzdGF0dXMiOiJzZW50X3NtcyIsImNyZWF0ZWRfYXQiOiIyMDI0LTA0LTE2VDAzOjA0OjE3LjY5NloiLCJ1cGRhdGVkX2F0IjoiMjAyNC0wNC0xNlQwMzowNDoxNy42OTZaIiwidW5pdmVyc2l0eSI6bnVsbCwidW5pdmVyc2l0eV9pZCI6bnVsbCwiaWF0IjoxNzE1MjM0NTUyLCJleHAiOjE3MTUyNzc3NTJ9.kSlVA51hoSq5a8XoUJgCmyabQZ4pOnkVPsHSza42jiQ"


origin = 'https://admin.iapply.org'


def download_image(url, folder, filename):
    try:
        # Ensure the folder exists, create it if not
        os.makedirs(folder, exist_ok=True)
        
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Construct the full path for saving the image
            save_path = os.path.join(folder, filename)
            # Open a file in binary write mode to save the image
            with open(save_path, 'wb') as file:
                # Write the content of the response to the file
                file.write(response.content)
            print("Image downloaded successfully!")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# image_url = 'https://images.globalstudypartners.com/webservice-manager/course-search/logos/providers/prod/pid-mi-au-9554-2d811a25-27a4-42d9-89b4-aec1423c436b-pid-mi-au-9554.png'
# save_path = 'Academies Australasia Polytechnic.png'
# folder_path = '/Users/jurakulovamadinabonu/python_projects/global_directions/uni_images'
# download_image(image_url,folder_path ,save_path)

def generate_random_string(length):
    # Generate a random string of uppercase letters
    return ''.join(random.choices(string.ascii_uppercase, k=length))
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

    return response

# a = uploadfile(token, 'university', 'logo', 'uni_images/Academies Australasia Polytechnic.png')
# ic(a.json())
# path = a.json()['path']
# ic(path)

def add_university(token, abbr_name_en, abbr_name_ru, abbr_name_uz, domain, email, full_name_en, full_name_ru, full_name_uz,
                   lead_limit,path_logo, location_id, login, password, representative_full_name='Avezov Murodjon'):
    url = "https://api.iapply.org/v1/universities"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Origin': origin
    }
    # data_file_upload = uploadfile(token, 'university', 'logo', file_name)
    # path = data_file_upload.json()
    # ic(path)
    # res = path['path']
    body = {
        'abbr_name_en': abbr_name_en,
        'abbr_name_ru': abbr_name_ru,
        'abbr_name_uz': abbr_name_uz,
        'domain': domain,
        'email': email,
        'full_name_en': full_name_en,
        'full_name_ru': full_name_ru,
        'full_name_uz': full_name_uz,
        'lead_limit': lead_limit,
        'location_id': location_id,
        'login': login,
        'logo': path_logo,
        'password': password,
        'representative_full_name': representative_full_name,
    }

    response = requests.post(url, headers=headers, json=body)

    return response.json(), response.status_code

# aadd_university = add_university(token, 'test3', 'test3', 'test3', 'test3.iapply.org', 'test3@gmail.com',
#                                 'test3', 'test3', 'test3', 1000, 'file.png', 1, 'info@test3.com', 'test3test3test3')

# dataUNI = aadd_university.json()
# ic(dataUNI)
# my_uni_id = dataUNI['id']


def update_data_university(uni_id,address_en,address_ru,address_uz,admission_deadline,admission_start_date,description_en,
                           description_ru,description_uz,gallery,has_accomodation,is_open_for_admission,latitude,longitude,
                           maximal_tuition_fee,minimal_tuition_fee,students_count,videoLink):
    url = f"https://api.iapply.org/v1/universities/{uni_id}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Origin': origin
    }
    body = {
        "address_en": address_en,
        "address_ru": address_ru,
        "address_uz": address_uz,
        "admission_deadline": admission_deadline,
        "admission_start_date": admission_start_date,
        "description_en": description_en,
        "description_ru": description_ru,
        "description_uz": description_uz,
        "gallery": gallery,
        "has_accomodation": has_accomodation,
        "is_open_for_admission": is_open_for_admission,
        "latitude": latitude,
        "longitude": longitude,
        "maximal_tuition_fee": maximal_tuition_fee,
        "minimal_tuition_fee": minimal_tuition_fee,
        "students_count": students_count,
        "videoLink": videoLink
    }

    response = requests.patch(url, headers=headers, json=body)

    return response

# update_uni = update_data_university(443, 'address en','address ru', 'address uz', '2024-11-01T10:17',
#                                     '2023-11-01T10:16','desc en','desc ru', 'desc uz', ['logo/4f4d9b05-48aa-41e8-9bf2-2e6cc2cbe353.png'],
#                                     True, False,'22','33',20000,1000,1023,"")
# res = update_uni.json()
# ic(res)


def update_meta(uni_id,mtdt_description_en,mtdt_description_ru,mtdt_description_uz,mtdt_title_en,mtdt_title_ru,mtdt_title_uz,
                payment_links,search_keys_en,search_keys_ru,search_keys_uz,exam_price=None):
    url = f"https://api.iapply.org/v1/universities/update/metadata/{uni_id}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Origin': origin
    }
    body = {
        'exam_price': exam_price,
        'mtdt_description_en': mtdt_description_en,
        'mtdt_description_ru': mtdt_description_ru,
        'mtdt_description_uz': mtdt_description_uz,
        'mtdt_title_en': mtdt_title_en,
        'mtdt_title_ru': mtdt_title_ru,
        'mtdt_title_uz': mtdt_title_uz,
        'payment_links': payment_links,
        'search_keys_en': search_keys_en,
        'search_keys_ru': search_keys_ru,
        'search_keys_uz': search_keys_uz
    }

    response = requests.patch(url, headers=headers, json=body)

    return response

# res = update_meta(443, 'mtdt_desc en','mtdt_desc ru', 'mtdt_desc uz','mdtd_title_uz','mtdt_title_ru','mtdt_title_uz',
#                   [],'search_keys_en','search_keys_ru','search_keys_uz')
# data_res = res.json()
# ic(data_res)

def return_uni_id(uni_name):
    with open('./all_status_uni.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
        for obj in data:
            # ic(obj)
            if obj['"full_name_en"'].lower().replace("\"", '') == uni_name.lower():
                return int(obj['"id"'])

array_obj = []
count_none = 0
with open('../GSP_NEW_universities_UPDATED.json', 'r', encoding='utf8') as f:
    data = json.load(f)
    for obj in tqdm(data):
        address_uz = obj['address_uz']
        address_en = obj['address_en']
        address_ru = obj['address_ru']
        admission_start_date = obj['admission_start_date']
        admission_deadline = obj['admission_deadline']
        admission_phone = obj['admission_phone']
        website_url = obj['website_url']
        description_en = obj['description_en']
        description_uz = obj['description_uz']
        description_ru = obj['description_ru']
        founded_year = obj['founded_year']
        has_accomodation = obj['has_accomodation']
        lead_limit = obj['lead_limit']
        gallery = obj['gallery']
        minimal_tuition_fee = obj['minimal_tuition_fee'] if obj['minimal_tuition_fee'] is not None else 13000
        maximal_tuition_fee = obj['maximal_tuition_fee'] if obj['maximal_tuition_fee'] is not None else 10000
        students_count = obj['students_count']
        abbr_name_uz = obj['abbr_name_uz']
        abbr_name_ru = obj['abbr_name_ru']
        abbr_name_en = obj['abbr_name_en']
        full_name_uz = obj['full_name_uz']
        full_name_ru = obj['full_name_ru']
        full_name_en = obj['full_name_en']
        logo = obj['logo']
        phone = obj['phone']
        email = obj['email']
        domain = obj['domain']
        login = obj['login']
        password = obj['password']
        current_quota = obj['current_quota']
        representative_full_name = obj['representative_full_name']
        latitude = obj['latitude']
        longitude = obj['longitude']
        is_open_for_admission = obj['is_open_for_admission']
        mtdt_title_uz = obj['mtdt_title_uz']
        mtdt_title_ru = obj['mtdt_title_ru']
        mtdt_title_en = obj['mtdt_title_en']
        mtdt_description_uz = obj['mtdt_description_uz']
        mtdt_description_ru = obj['mtdt_description_ru']
        mtdt_description_en = obj['mtdt_description_en']
        search_keys_uz = obj['search_keys_uz']
        search_keys_ru = obj['search_keys_ru']
        search_keys_en = obj['search_keys_en']
        location_id = obj['location_id']
        ic(full_name_ru)
        abbr = generate_random_string(8)
        ic(abbr)
        # res_add_uni, status = add_university(
        #     token,
        #     full_name_uz=full_name_uz,
        #     full_name_ru=full_name_uz,
        #     full_name_en=full_name_uz,
        #     domain=domain,
        #     email=email,
        #     abbr_name_en=abbr,
        #     abbr_name_ru=abbr,
        #     abbr_name_uz=abbr,
        #     lead_limit=lead_limit,
        #     path_logo=logo,
        #     location_id=location_id,
        #     login=f'info@{abbr}.com',
        #     password=password,
        #     representative_full_name=representative_full_name
        # )
        
        
        # status1 = False
        # status2 = False
        # status3 = False

        # if status == 201:
        #     status1 = True
        #     # response_data = res_add_uni.json()  # Correctly parsing the JSON only once
        #     ic(res_add_uni)                   # Inspect the parsed JSON data
        #     uni_id = res_add_uni['id']   
        #     ic(uni_id)     # Accessing the 'id' from the parsed JSON
        #     obj = {
        #         'uni_id': uni_id,
        #         "uni_nme": full_name_uz
        #     }
        #     ic(obj)
        #     array_obj.append(obj)
        #     with open('inserted_uni.json', 'w', encoding='utf-8') as f:
        #         json.dump(array_obj, f, ensure_ascii=False)
        # else:
        #     # response_data, status = res_add_uni
        #     status1 = False
        #     obj = {
        #         "uni_name": full_name_uz,
        #         "error_mess": res_add_uni['message']
        #     }
        #     ic(obj)
        #     array_obj.append(obj)
        #     with open('inserted_uni.json', 'w', encoding='utf-8') as f:
        #         json.dump(array_obj, f, ensure_ascii=False)
        # if status1:
        #     time.sleep(1)
        #     # res_add_uni = res_add_uni.
        #     uni_id = res_add_uni['id']

                    
        uni_ids = return_uni_id(full_name_uz)
        ic(uni_ids, type(uni_ids)) 
        if uni_ids is None:
            count_none += 1
            continue
        ic(uni_ids, type(uni_ids))
        update_uni = update_data_university(
            
            uni_id=int(uni_ids),
            address_en=address_en,
            address_ru=address_ru,
            address_uz=address_uz,
            admission_deadline=admission_deadline,
            admission_start_date=admission_start_date,
            description_en=description_en,
            description_ru=description_ru,
            description_uz=description_uz,
            gallery=[gallery],
            has_accomodation=has_accomodation,
            is_open_for_admission=is_open_for_admission,
            latitude=str(latitude) if latitude is not None else "11",
            longitude=str(longitude) if longitude is not None else "13",
            maximal_tuition_fee=maximal_tuition_fee if maximal_tuition_fee else 10000,
            minimal_tuition_fee=minimal_tuition_fee if minimal_tuition_fee else 13000,
            students_count=students_count,
            videoLink=''
        )
        # time.sleep(1)
        ic(update_uni.json())
        #     if update_uni.json() == 1:
        #         status2 = True
        #     else:
        #         status2 = False
        #         # continue
        # if status2:
        time.sleep(1)
        update_meta_ = update_meta(
            uni_id=int(return_uni_id(full_name_uz)),
            mtdt_description_en=mtdt_description_en,
            mtdt_description_ru=mtdt_description_ru,
            mtdt_description_uz=mtdt_description_uz,
            mtdt_title_en=mtdt_title_en,
            mtdt_title_ru=mtdt_title_ru,
            mtdt_title_uz=mtdt_title_uz,
            payment_links=None,
            search_keys_en=search_keys_en,
            search_keys_ru=search_keys_ru,
            search_keys_uz=search_keys_uz,
            exam_price=None
        )
        ic(update_meta_.json())
        #     if update_meta_.json() == 1:
        #         status3 = True
        #     else:
        #         status3 = False
        # time.sleep(1)
ic(count_none)