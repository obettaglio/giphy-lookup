"""GIPHY search app."""

from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, request
import requests


app = Flask(__name__)
app.secret_key = 'aifowjfniogengrioawhniorh'
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Displays homepage.

    Homepage contains Search GIFs field and GO submit button."""

    return render_template('homepage.html')


@app.route('/search-giphy', methods=['POST'])
def search_giphy():
    """Requests GIF url from GIPHY API.

    API: http://api.giphy.com/v1/gifs/search?q=[KEYWORD_HERE]&api_key=dc6zaTOxFJmzC&limit=1
    
    Further options:
        -optimize search terms by capitalization, punctuation, etc.
    """

    search = request.form.get('search')

    search = search.split(' ')
    url_search = '+'.join(search)

    parameters = {'q': url_search,
                  'api_key': 'dc6zaTOxFJmzC',
                  'limit': '1'}

    response = requests.get('http://api.giphy.com/v1/gifs/search', params=parameters)
    data = response.json()
    print data

    url = data['data'][0]['embed_url']
    print url

    return jsonify(url)


if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    app.run(port=5000, host='0.0.0.0')
