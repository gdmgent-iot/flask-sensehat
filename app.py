from flask import Flask, render_template, jsonify, request
from sense_hat import SenseHat

app = Flask(__name__)

showing_message = False

sense = SenseHat()

@app.route('/')
def main():
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()
    return render_template('interface.html', temperature=temperature, pressure=pressure, humidity=humidity)

@app.route('/api/send_message', methods=['POST'])
def send_message():
    global showing_message
    # set orientation of the message
    sense.set_rotation(0)
    #message was sent via json in 'message' key
    message = request.json['message']
    txtColor = request.json['color']
    if not showing_message:
        showing_message = True
        sense.show_message(message, text_colour=txtColor)
    showing_message = False

    return jsonify({'message': message})

if __name__ == "__main__" :
    app.run(host="0.0.0.0", debug=True, port=80)