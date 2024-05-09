import requests
import json
from tqdm import tqdm
import sqlite3
from icecream import ic
from add_direcition import add_direction,  update_direction
connection = sqlite3.connect('university_data1.db')
cursor = connection.cursor()


all_directions_query = "SELECT * FROM directions;"
data = cursor.execute(all_directions_query).fetchall()
for row in data:
    direction_id = row[0]
    university_id = row[1]
    direction_name = row[2]
    tuition_fee = row[3] if row[3] is not None else 0
    application_fee = row[4] if row[4] is not None else 0
    if tuition_fee == 0 or tuition_fee is None:
        continue
    if 'Master' in direction_name or 'MBA' in direction_name:
        degree_id=2
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
    res_add_dir = add_direction(
        application_fee=application_fee,
        category_id=14,
        contract_type_ids=2,
        degree_ids=degree_id,
        description_en="  ",
        description_ru="  ",
        description_uz="  ",
        education_type_languages=[{'education_type_id': 1, 'education_language_id': 2}],
        education_type_tuition_fees=[{'education_type_id': 1, 'local_tuition_fee': tuition_fee, 'international_tuition_fee': None}],
        end_date="2024-11-01",
        first_subject='Matematika',
        has_mandatory_subjects=True,
        has_stipend=False,
        # id_number=
    )