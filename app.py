from flask import Flask, render_template, jsonify, request
from sense_hat import SenseHat

app = Flask(__name__)

sense = SenseHat()

@app.route('/')
def main():
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()
    return render_template('interface.html', temperature=temperature, pressure=pressure, humidity=humidity)

@app.route('/api/send_message', methods=['POST'])
def send_message():
    #message was sent via json in 'message' key
    message = request.json['message']
    sense.show_message(message)
    return jsonify({'message': message})

if __name__ == "__main__" :
    # send welcome to he led matrix, red and blue letters
    sense.show_message("Welcome to my first Flask site", text_colour=[255, 0, 0], back_colour=[0, 0, 255])
    app.run(host="0.0.0.0", debug=True, port=80)