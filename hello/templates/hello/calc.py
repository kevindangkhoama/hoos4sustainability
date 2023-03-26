from flask import Flask, request, render_template
import googlemaps

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    transportation = request.form['transportation']
    point_a = request.form['point_a']
    point_b = request.form['point_b']
    
    API_KEY = 'your_api_key_here'
    client = googlemaps.Client(API_KEY)
    
    result = client.directions(point_a, point_b)
    distance = result[0]['legs'][0]['distance']['text']
    points_earned = float(distance.replace(' mi', ''))
    
    switcher = {
        "active": points_earned * 10,
        "public": points_earned * 5,
        "shared": points_earned * 2,
    }
    
    points = switcher.get(transportation, 0)
    
    return render_template('result.html', points=points)

if __name__ == '__main__':
    app.run(debug=True)
