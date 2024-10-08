from flask import Flask, render_template, jsonify
from sense_hat import SenseHat

app = Flask(__name__)

sense = SenseHat()

@app.route('/')
def main():
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()
    return render_template('interface.html', temperature=temperature, pressure=pressure, humidity=humidity)

if __name__ == "__main__" :
    # send welcome to he led matrix, red and blue letters
    sense.show_message("Welcome to my first Flask site", text_colour=[255, 0, 0], back_colour=[0, 0, 255])
    app.run(host="0.0.0.0", debug=True, port=80)