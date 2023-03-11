from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['company']
        url = 'https://www.alphavantage.co/query'
        params = {
            'function': 'NEWS_SENTIMENT',
            'tickers': user_input,
            'apikey': 'TE1E1KD330UYLRHQ'
        }
        response = requests.get(url, params=params)
        data = response.json()
        feed = data['feed']
        return render_template('output.html', news=feed)
    else:
        return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)
