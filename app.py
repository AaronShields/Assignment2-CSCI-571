from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Route to render the HTML form
@app.route('/')
def index():
    return render_template('weather_form.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    lat = request.args.get('lat')
    lng = request.args.get('lng')

    print(lat + lng); 

    # Make a request to Tomorrow.io API
    response = requests.get(tomorrow_api_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return jsonify(weather_data)
    else:
        return jsonify({"error": "Failed to retrieve weather data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
