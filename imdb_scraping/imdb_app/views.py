from django.shortcuts import render
from .utils import get_plot
# Create your views here.
def home_view(request):
    import pandas as pd
    import numpy as np
    from bs4 import BeautifulSoup as bs
    import requests

    url = 'https://www.imdb.com/chart/top/'
    response = requests.get(url)
    response.status_code

    page = response.text
    doc = bs(page, 'html.parser')
    len(page)

    movie_name_parent = doc.find_all('td', {'class': 'titleColumn'})
    movie_rating_parent = doc.find_all('td', {'class': 'ratingColumn imdbRating'})
    movie_name = []
    movie_year = []
    movie_rating = []
    for i in movie_name_parent:
        movie_name.append(i.a.text.strip())
        movie_year.append(i.span.text.strip().replace('(', '').replace(')', ''))


    for j in movie_rating_parent:
        movie_rating.append(j.strong.text)
    
    movie_dictionary = {
    'movie_name' : movie_name,
    'movie_release_year' : movie_year,
    'movie_rating' : movie_rating
    }
    data = pd.DataFrame(movie_dictionary)

    data['movie_rating'] = data['movie_rating'].astype(float)
    data['movie_release_year'] = data['movie_release_year'].astype(int)

    x = data['movie_rating']
    y = data['movie_release_year']
    chart = get_plot(x,y)
    return render(request, 'index.html', {'chart':chart, 'data':data})