import json
from icecream import ic
# from add_university import token, origin
import requests
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZmlyc3RfbmFtZSI6IlNoYWtoem9kIiwibGFzdF9uYW1lIjoiWW92a29jaGV2IiwicGhvbmUiOiIrOTk4OTc3MzQ4NDAxIiwiZW1haWwiOiJzeW92a29jaGV2QGdtYWlsLmNvbSIsImF2YXRhciI6bnVsbCwicm9sZSI6InN1cGVyX2FkbWluIiwiaXNfdmVyaWZ5Ijp0cnVlLCJzdGF0dXMiOiJzZW50X3NtcyIsImNyZWF0ZWRfYXQiOiIyMDI0LTA0LTE2VDAzOjA0OjE3LjY5NloiLCJ1cGRhdGVkX2F0IjoiMjAyNC0wNC0xNlQwMzowNDoxNy42OTZaIiwidW5pdmVyc2l0eSI6bnVsbCwidW5pdmVyc2l0eV9pZCI6bnVsbCwiaWF0IjoxNzE1MjM0NTUyLCJleHAiOjE3MTUyNzc3NTJ9.kSlVA51hoSq5a8XoUJgCmyabQZ4pOnkVPsHSza42jiQ"
origin = 'https://admin.iapply.org'
# from add_university import update_data_university, update_meta
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
def return_data_uni(uni_name):
    with open('../real_time_uni_add_UDPATED.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        for obj in data:
           
            if obj['full_name_en'].lower() == uni_name.lower():
                ic(obj['full_name_uz'], uni_name)
                return obj
        return None
    

with open('./uni_id_extra.json', 'r', encoding='utf-8-sig') as f:
    data_extra = json.load(f)
for obj in data_extra:
    uni_name = obj.get('\"full_name_en\"', '')  # Accessing keys without extra quotes
    uni_id = obj.get('\"id\"', '')  # Accessing keys without extra quotes
    data_uni = return_data_uni(uni_name)

    # ic(data_uni)
    if data_uni is not None:
        # for obj_ in data_uni:
        #     obj = obj_
        # ic(obj)
        obj = data_uni
        address_uz = obj['address_uz']
        address_en = obj.get('address_en')
        address_ru = obj.get('address_ru')
        admission_start_date = obj.get('admission_start_date')
        admission_deadline = obj.get('admission_deadline')
        admission_phone = obj.get('admission_phone')
        website_url = obj.get('website_url')
        description_en = obj.get('description_en')
        description_uz = obj.get('description_uz')
        description_ru = obj.get('description_ru')
        founded_year = obj.get('founded_year')
        has_accomodation = obj.get('has_accomodation')
        lead_limit = obj.get('lead_limit')
        gallery = obj.get('gallery')
        minimal_tuition_fee = obj.get('minimal_tuition_fee') if obj.get('minimal_tuition_fee') is not None else 13000
        maximal_tuition_fee = obj.get('maximal_tuition_fee') if obj.get('maximal_tuition_fee') is not None else 10000
        students_count = obj['students_count']
        abbr_name_uz = obj.get('abbr_name_uz')
        abbr_name_ru = obj.get('abbr_name_ru')
        abbr_name_en = obj.get('abbr_name_en')
        full_name_uz = obj.get('full_name_uz')
        full_name_ru = obj.get('full_name_ru')
        full_name_en = obj.get('full_name_en')
        logo = obj.get('logo')
        phone = obj.get('phone')

        domain = obj.get('domain')
        login = obj.get('login')
        password = obj.get('password')
        current_quota = obj.get('current_quota')
        representative_full_name = obj.get('representative_full_name')
        latitude = obj.get('latitude')
        longitude =obj.get('longitude')
        is_open_for_admission = obj.get('is_open_for_admission')
        mtdt_title_uz = obj.get('mtdt_title_uz')
        mtdt_title_ru = obj.get('mtdt_title_ru')
        mtdt_title_en = obj.get('mtdt_title_en')
        mtdt_description_uz = obj.get('mtdt_description_uz')
        mtdt_description_ru = obj.get('mtdt_description_ru')
        mtdt_description_en = obj.get('mtdt_description_en')
        search_keys_uz = obj.get('search_keys_uz')
        search_keys_ru = obj.get('search_keys_ru')
        search_keys_en = obj.get('search_keys_en')
        location_id = obj.get('location_id')
        update_uni_data = update_data_university(
            
        
        uni_id=uni_id,
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
        ic(update_uni_data.json())
        update_meta_ = update_meta(
        uni_id=uni_id,
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