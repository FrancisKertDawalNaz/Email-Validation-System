from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "4a308b1771dfb65d6ed51673e9de836d"

@app.route('/', methods=['GET', 'POST'])
def index():

    result = None

    if request.method == 'POST':

        email = request.form['email']

        url = f"http://apilayer.net/api/check?access_key={API_KEY}&email={email}&smtp=1&format=1"

        response = requests.get(url)

        data = response.json()

        result = data

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)