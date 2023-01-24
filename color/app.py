#!/usr/bin/env python3
import os
from flask import Flask, request, render_template

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

color = os.environ.get('APP_COLOR')
#name = os.environ.get('NAME')

@app.route("/")
def main():
	print(color)
	return render_template('hello.html',app_color=color_codes[color])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='4043')
