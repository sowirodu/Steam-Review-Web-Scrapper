import csv
import requests

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
        'review_type': 'positive',
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

n = 200

reviews = []
ids = open('idList.txt', 'r')
idTxt = ids.readlines()

for id in idTxt:
    reviews.extend(get_n_reviews(id, n)) 

# Output reviews to a CSV file
filename = 'reviews.csv'
fieldnames = reviews[0].keys()

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(reviews)

print(f"Reviews saved to {filename}")