import requests
import json
from tqdm import tqdm
import random
import sqlite3
from icecream import ic
from datetime import datetime
from add_direcition import add_direction,  update_direction
connection = sqlite3.connect('university_data1.db')
cursor = connection.cursor()

# with open()

# def return_university_id(university_name):

all_directions_query = "SELECT * FROM directions;"
data = cursor.execute(all_directions_query).fetchall()

def return_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def generate_number():
    return random.randint(10000000, 99999999)
array = []
for row in data:
    direction_id = row[0]
    university_id = row[1]
    direction_name = row[2]
    tuition_fee = row[3] if row[3] is not None else 0
    application_fee = row[4] if row[4] is not None else 0
    if tuition_fee == 0 or tuition_fee is None:
        continue
    masters_keywords = {'Master', 'MBA', 'Undergraduate'}
    doctorate_keywords = {'Doctor', 'PhD', 'Ph.D', 'Postgraduate'}

    # Check the degree type
    if any(keyword in direction_name for keyword in masters_keywords):
        degree_id = 2
        number_gen = f"7{generate_number()}"
    elif any(keyword in direction_name for keyword in doctorate_keywords):
        degree_id = 3
        number_gen = f"8{generate_number()}"
    else:
        degree_id = 1
        number_gen = f"6{generate_number()}"

    ielts = row[8]
    pte = row[9]
    toefl = row[10]
    cae = row[11]
    dolingo = row[12]
    requirements = ''
    if ielts is not None:
        requirements += 'ielts: ' + str(ielts) + ', '
    if pte is not None:
        requirements += 'pte: ' + str(pte) + ', '
    if toefl is not None:
        requirements += 'toefl: ' + str(toefl) + ', '
    if cae is not None:
        requirements += 'cae: ' + str(cae) + ', '
    if dolingo is not None:
        requirements += 'dolingo: ' + str(dolingo) + ', '
    if tuition_fee is not None:
        tuition_fee = tuition_fee
    else:
        tuition_fee = 0
    if application_fee is not None:
        application_fee = application_fee
    else:
        application_fee = 0
    if requirements == '':
        requirements = '  '
    res_add_dir, data = update_direction(
        application_fee=application_fee,
        category_id=14,
        contract_type_ids=2,
        degree_ids=degree_id,
        description_en="  ",
        description_ru="  ",
        description_uz="  ",
        education_type_languages=[{'education_type_id': 1, 'education_language_id': 2}],
        education_type_tuition_fees=[{'education_type_id': 1, 'local_tuition_fee': tuition_fee, 'international_tuition_fee': None}],
        end_date="2024-06-01",
        first_subject='Matematika',
        has_mandatory_subjects=True,
        has_stipend=False,
        id_number=number_gen,
        is_open_for_admission=True,
        name_en=direction_name,
        name_uz=direction_name,
        name_ru=direction_name,
        requirement_en=requirements,
        requirement_ru=requirements,
        requirement_uz=requirements,
        second_subject='Fizika',
        start_date="2023-11-01",
        status="active",
        university_id=university_id
    )
    file_name = return_time()
    array.append({
        'res': res_add_dir,
        'data': data
    })
    with open(f'updated_directions_{file_name}.json', 'w', encoding='utf8') as f:
        json.dump(array, f, ensure_ascii=False)