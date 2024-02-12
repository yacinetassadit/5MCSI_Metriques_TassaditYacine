from flask import Flask, render_template_string, render_template, jsonify
#from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
#import requests
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #TassaditYACINE2

@app.route("/contact/")
def contact():
    return render_template("Contact.html")

@app.route('/paris/') #problème de token donc ça ne fonctionne pas!
def meteo():
    response = urlopen('https://api.openweathermap.org/data/2.5/forecast/daily?q=Paris,fr&cnt=16&appid=bd5e378503939ddaee76f12ad7a97608')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('temp', {}).get('day') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")


@app.route('/histogramme')
def histogramme():
    # Récupérer les données de l'API
    url = 'https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx'  
    response = urlopen(url)
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    
    # Extraction des températures
    temperatures = [data['main']['temp'] for data in json_content['list']]
    
    # Passer les données à la template HTML
    return render_template('histogramme.html', temperatures=temperatures)

  
if __name__ == "__main__":
  app.run(debug=True)
