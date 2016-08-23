#! python3
# movies.py - Checks what movies are out at my usual theater with times

import urllib
import urllib.request
from bs4 import BeautifulSoup

url = "http://movies.eventful.com/theaters-showtimes/amc-easton-town-center-30-with-dinein-theatres-/T0-001-000002798-1"

open = urllib.request.urlopen(url)
soup = BeautifulSoup(open,'html.parser')
table_body = soup.find('tbody')
rows = table_body.find_all('tr')

for movie in rows:
    name = []
    name.append(movie.find('div', {'class':'movie-title'}).text.strip('\n'))

    showtimes = []
    showtimes.append(movie.find('a',{'data-ga-label':'Showtimes Link'}).text)

    print('Movie name: ' + str(name))
    print('Showtimes: ' + str(showtimes))

"""
TODO-
- Pull in RottenTomatoes or IMDB rating
- Note if the movie came out in the last 3 days
"""