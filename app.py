# app.py
from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)

def load_countries_data():
    with open('countries.json', 'r') as file:
        return json.load(file)

countries_data = load_countries_data()

def get_capital(country):
    for entry in countries_data:
        if entry['country'].lower() == country.lower():
            return entry['capital']
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/capital', methods=['GET'])
def capital():
    country = request.args.get('country')
    if not country:
        return jsonify({'error': 'Country parameter is required'}), 400
    capital = get_capital(country)
    if capital is None:
        return jsonify({'error': 'Invalid country or no data available'}), 400
    return jsonify({'country': country, 'capital': capital})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
