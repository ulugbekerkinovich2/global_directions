import requests
from icecream import ic
import json

array = []
def get_all_uni(page):
    url = f"https://iapply.org/_next/data/8xtVT4nKmAOSRmSudKrlm/en/universities.json?page={page}"
    response = requests.get(url)
    data = response.json()
    return data
try:
    for i in range(1, 1000):
        res = get_all_uni(i)
        data = res['pageProps']['data']
        univers = data['universities']
        array.append(univers)

        with open('all_iapply_data.json', 'w', encoding='utf8') as f:
            json.dump(array, f, ensure_ascii=False)
except Exception as e:
    ic(e)
