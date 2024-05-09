import requests
from icecream import ic
import time
import json
import sqlite3
from tqdm import tqdm
connection = sqlite3.connect('../university_data1.db')
cursor = connection.cursor()

def download_image(url, filename):
    """Download an image from a specified URL and save it to a local file.

    Args:
    url (str): URL of the image to be downloaded.
    filename (str): Local filename to save the downloaded image.

    Returns:
    bool: True if the download was successful, False otherwise.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'../images_logo/{filename}', 'wb') as file:
                file.write(response.content)
            print("Image downloaded successfully.")
            return True
        else:
            print("Failed to download image. Status code:", response.status_code)
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage


select_university_name_and_profile_image = """
SELECT university_name, profile_image
FROM universities
"""

data = cursor.execute(select_university_name_and_profile_image)
rows = data.fetchall()

array = []
for row in rows:
    university_name = row[0]
    profile_image = row[1]
    filename = f"{university_name}.jpg"
    download_image(profile_image, filename)
    # time.sleep(0.5)
    obj = {
        'university_name': university_name,
        'profile_image': filename
    }
    array.append(obj)
    with open('universities_images.json', 'w', encoding='utf8') as f:
        json.dump(array, f, ensure_ascii=False)

# with open('uni_profiles.json', 'w', encoding='utf8') as f:
#     json.dump(array, f, ensure_ascii=False)
# Close the cursor and connection to the database
cursor.close()
connection.close()

