from flask import Flask, render_template, request, jsonify
from script import *
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getColors')
def add_numbers():

    user = request.args.get("handle", 0, type = str)

    user = ShadesOfGray(user)

    return jsonify(
    	num_grays = user.data["num_grays"],
    	num_colors = user.data["num_colors"],
    	avatar_url = user.url
    )

if __name__ == '__main__':
	# post = int(os.environ.get("PORT", 5000))
	# app.run(debug=True, host='0.0.0.0', port=port)
	app.run()
