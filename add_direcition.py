import requests
import json
from icecream import ic
import time
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZmlyc3RfbmFtZSI6IlNoYWtoem9kIiwibGFzdF9uYW1lIjoiWW92a29jaGV2IiwicGhvbmUiOiIrOTk4OTc3MzQ4NDAxIiwiZW1haWwiOiJzeW92a29jaGV2QGdtYWlsLmNvbSIsImF2YXRhciI6bnVsbCwicm9sZSI6InN1cGVyX2FkbWluIiwiaXNfdmVyaWZ5Ijp0cnVlLCJzdGF0dXMiOiJzZW50X3NtcyIsImNyZWF0ZWRfYXQiOiIyMDI0LTA0LTE2VDAzOjA0OjE3LjY5NloiLCJ1cGRhdGVkX2F0IjoiMjAyNC0wNC0xNlQwMzowNDoxNy42OTZaIiwidW5pdmVyc2l0eSI6bnVsbCwidW5pdmVyc2l0eV9pZCI6bnVsbCwiaWF0IjoxNzE1MjM0NTUyLCJleHAiOjE3MTUyNzc3NTJ9.kSlVA51hoSq5a8XoUJgCmyabQZ4pOnkVPsHSza42jiQ"


origin = 'https://admin.iapply.org'

def add_direction(application_fee,category_id,contract_type_ids,degree_ids,description_en,description_ru,description_uz,education_type_languages,
                  education_type_tuition_fees,end_date,first_subject,has_mandatory_subjects,has_stipend,id_number,is_open_for_admission,
                  name_en,name_ru,name_uz,requirement_en,requirement_ru,requirement_uz,second_subject,start_date,status,university_id):
    url = "https://api.iapply.org/v1/directions"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Origin': origin    
    }
    body = {
        "application_fee": application_fee,
        "category_id": category_id,
        "contract_type_ids": [contract_type_ids],
        "degree_ids": [degree_ids],
        "description_en": description_en,
        "description_ru": description_ru,
        "description_uz": description_uz,
        "education_type_languages": education_type_languages,
        "education_type_tuition_fees": education_type_tuition_fees,
        "end_date": end_date,
        "first_subject": first_subject,
        "has_mandatory_subjects": has_mandatory_subjects,
        "has_stipend": has_stipend,
        "id_number": id_number,
        "is_open_for_admission": is_open_for_admission,
        "name_en": name_en,
        "name_ru": name_ru,
        "name_uz": name_uz,
        "requirement_en": requirement_en,
        "requirement_ru": requirement_ru,
        "requirement_uz": requirement_uz,
        "second_subject": second_subject,
        "start_date": start_date,
        "status": status,
        "university_id": university_id
    }
    response = requests.post(url, headers=headers, json=body)
    time.sleep(0.5)
    return response
res_direction = add_direction(1200,1,[2],[1],'desc_en','desc_ru','desc_uz',[{'education_type_id':1,'education_language_id':2}],[{'education_type_id':1,'local_tuition_fee':1200,'international_tuition_fee':None}],'2024-11-01',
                              "Matematika",True,False,"6090930",False,"Dasturlash en1",'Dasturlash ru1','Dasturlash uz1','req_en_','req_ru_',
                               'req_uz','','2023-11-01',"active",443)
res = res_direction.json()
ic(res)

def update_direction(dir_id,application_fee,category_id,contract_type_ids,degree_ids,description_en,description_ru,description_uz,education_type_languages,
                  education_type_tuition_fees,end_date,first_subject,has_mandatory_subjects,has_stipend,id_number,is_open_for_admission,
                  name_en,name_ru,name_uz,requirement_en,requirement_ru,requirement_uz,second_subject,start_date,status,university_id):
    url = f"https://api.iapply.org/v1/directions/{dir_id}"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'Origin': origin    
    }
    body = {
        "application_fee": application_fee,
        "category_id": category_id,
        "contract_type_ids": contract_type_ids,
        "degree_ids": degree_ids,
        "description_en": description_en,
        "description_ru": description_ru,
        "description_uz": description_uz,
        "education_type_languages": education_type_languages,
        "education_type_tuition_fees": education_type_tuition_fees,
        "end_date": end_date,
        "first_subject": first_subject,
        "has_mandatory_subjects": has_mandatory_subjects,
        "has_stipend": has_stipend,
        "id_number": id_number,
        "is_open_for_admission": is_open_for_admission,
        "name_en": name_en,
        "name_ru": name_ru,
        "name_uz": name_uz,
        "requirement_en": requirement_en,
        "requirement_ru": requirement_ru,
        "requirement_uz": requirement_uz,
        "second_subject": second_subject,
        "start_date": start_date,
        "status": status,
        "university_id": university_id
    }
    response = requests.patch(url, headers=headers, json=body)

    return response



