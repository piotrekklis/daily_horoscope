from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup
import random

flask_app = Flask(__name__)
@flask_app.route('/horoscope', methods=['GET'])
def get_horoscope():
    
    signs = ['koziorozec', 'wodnik', 'ryby', 'baran', 'byk', 'bliznieta', 'rak', 'lew', 'panna', 'waga', 'skorpion', 'strzelec']
    corpus = []

    for i in signs:

        page = requests.get('https://horoskop.wp.pl/horoskop/horoskop-dzienny/' + i)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(id='artykul_srodek')

        elems = results.find_all('p')
        horoscope = elems[0].text

        random_horoscope_list = horoscope.split('.')

        for r in random_horoscope_list:
            if r.strip() != '':
                a = r.strip()
                corpus.append(a.capitalize())

    final_horoscope = []
    while len(final_horoscope) != 4:
        a = random.randrange(0, len(corpus), 1)
        if a not in final_horoscope:
            final_horoscope.append(a)
    
    compose_horoscope = corpus[int(final_horoscope[0])] + '. ' + corpus[int(final_horoscope[1])] + '. ' + corpus[int(final_horoscope[2])] + '. ' + corpus[int(final_horoscope[3])] + '. '
        
    # return render_template('horoscope.html', text=compose_horoscope)
    return jsonify({'horoscope': compose_horoscope})

@flask_app.route('/')
def index():

    return render_template('horoscope.html')
