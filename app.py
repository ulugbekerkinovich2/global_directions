from add_direcition import add_direction,update_direction
import json
import time
from icecream import ic
with open('../gsp_directions.json','r', encoding='utf-8') as f:
    array = json.load(f)

with open('../univers.json', 'r', encoding='utf-8') as f:
    data_univers_iapply = json.load(f)
array_id = []
for obj in array:
    id_number = obj.get('id_number')
    university_id = obj.get('university_id')
    first_subject = obj.get('first_subject')
    second_subject = obj.get('second_subject')
    name_uz = obj.get('name_uz')
    ic(name_uz)
    name_ru = obj.get('name_ru')
    name_en = obj.get('name_en')
    has_stipend = obj.get('has_stipend')
    has_mandatory_subjects = obj.get('has_mandatory_subjects')
    is_open_for_admission = obj.get('is_open_for_admission')
    requirement_ru = obj.get('requirement_ru')
    requirement_uz = obj.get('requirement_uz')
    requirement_en = obj.get('requirement_en')
    category_id = obj.get('category_id')
    degree_ids = obj.get('degree_ids')
    contract_type_ids = obj.get('contract_type_ids')
    start_date = obj.get('start_date')
    end_date = obj.get('end_date')
    education_type_languages = obj.get('education_type_languages')
    education_type_tuition_fees = obj.get('education_type_tuition_fees')
    res = add_direction(

        0,
        1,
        contract_type_ids,
        degree_ids,
        ' ',
        ' ',
        ' ',
        education_type_languages,
        education_type_tuition_fees,
        end_date,
        first_subject,
        has_mandatory_subjects,
        has_stipend,
        str(id_number),
        is_open_for_admission,
        name_en,
        name_ru,
        name_uz,
        requirement_en,
        requirement_ru,
        requirement_uz,
        second_subject,
        start_date,
        'active',
        university_id
    )
    
    ic(university_id)
    data  = res.json()
    
    if data.get('error') == 'Conflict' or data.get('message') == 'Internal server error':
        # ic(data)
        continue
    ic(data)
    ic('kedli')
    time.sleep(4)
    direction_id = data['id']
    obj = {
        'direction_id': direction_id,
        'university_id': university_id
    }
    if direction_id:
        ic('direction_id', direction_id)
        array_id.append(obj)
        time.sleep(3)
    ic(obj)
    with open('added_gsp_directions_id1.json', 'w', encoding='utf8') as f:
        json.dump(array_id, f, ensure_ascii=False)


