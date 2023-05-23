import csv
import requests
import pandas as pd

def get_reviews(appid, params={'json':1}):
    url = 'https://store.steampowered.com/appreviews/'
    response = requests.get(url=url+appid, params=params, headers={'User-Agent': 'Mozilla/5.0'})
    return response.json()

def get_n_reviews(appid, n):
    reviews = []
    cursor = '*'
    params = {
        'json': 1,
        'filter': 'all',
        'language': 'english',
        'day_range' : 9223372036854775807,
        'review_type': 'positive',
        'purchase_type' : 'all'
    }

    while n > 0:
        params['cursor'] = cursor.encode()
        params['num_per_page'] = 100
        n -= 100

        response = get_reviews(str(appid), params)
        cursor = response['cursor']
        reviews += response['reviews']

        if len(response['reviews']) < 100:
            break

    return reviews

n = 300

ids = open('idList.txt', 'r')
idTxt = ids.readlines()

# Create a dictionary to store reviews for each app ID
reviews_dict = {}

for id in idTxt:
    app_reviews = get_n_reviews(id, n)
    reviews_dict[id.strip()] = app_reviews

# Save reviews in different sheets of an Excel file
filename = 'reviews.xlsx'

with pd.ExcelWriter(filename) as writer:
    for app_id, reviews in reviews_dict.items():
        df = pd.DataFrame(reviews)
        df.to_excel(writer, sheet_name=app_id, index=False)

print(f"Reviews saved to {filename}")
