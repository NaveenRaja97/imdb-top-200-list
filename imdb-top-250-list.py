import pandas as pd
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
#print(response)         # <Response [200]>
data = BeautifulSoup(response.content,'html.parser')            # gets all data from web page

name = data.find_all('td',class_='titleColumn')                 # for names
movie_name = []
for i in range(0,len(name)):
    movie_name.append(name[i].a.get_text())

rating = data.find_all('td',class_='ratingColumn imdbRating')   # for ratings
movie_rating = []
for i in range(0,len(rating)):
    movie_rating.append(rating[i].strong.get_text())

year = data.find_all('span',class_='secondaryInfo')             # for year
movie_year = []
for i in range(0,len(year)):
    movie_year.append(year[i].get_text())

image = data.find_all('td',class_='posterColumn')               # for image
movie_image = []
for i in range(0,len(image)):
    movie_image.append(image[i].img['src'])

df           = pd.DataFrame()                                   # creating dataframe
df['Name']   = movie_name
df['Rating'] = movie_rating
df['Year']   = movie_year
df['Image']  = movie_image

df.to_csv('IMDB_TOP_250_MOVIES_LIST.csv')                       # exporting data to csv file