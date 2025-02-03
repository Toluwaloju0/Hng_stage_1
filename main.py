#!/usr/bin/env python3
"""The maon module to launch the app"""

import math
from armstrong import armstrong, is_even
from flask import Flask, request, jsonify, abort
from prime import is_prime
from perfect import is_perfect
from request import number_api
from sum import digit_sum
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

# Tell flask it is behind a proxy before starting the app
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

# set the error handler for 400 to handle alphabet, symbols and mixed characters
@app.errorhandler(400)
def bad_request(e):
    if request.args.get('number') == None:
        return jsonify({
            'number': None,
            'error': True
        }), 400
    elif request.args.get('number').isalpha() == True:
        return jsonify({
            'number': 'alphabet',
            'error': True
        }), 400
    elif request.args.get('number').isalnum() == False:
        return jsonify({
            'number': 'symbol',
            'error': True
        }), 400
    else:
        return jsonify({
            'number': 'mixed',
            'error': True
        }), 400

# create a route to the /api/classify-number
@app.route('/api/classify-number', strict_slashes=False)
def fun_fact():
    # check if the number argument exists and is not a digit
    if request.args.get('number') == None or request.args.get('number').isdigit() == False:
        abort(400)
    
    #convert to integer and pass to the appopraite functions to process the number
    num = int(request.args.get('number'))
    properties = []
    if armstrong(num):
        properties.append('armstrong')
    properties.append('even' if is_even(num) else 'odd')
    # create a dictionary to store the number properties
    my_dict = {
        "number": num,
        "is_prime": is_prime(num),
        "digit_sum": digit_sum(num),
        "fun_fact": number_api(num),
        "is_perfect": is_perfect(num),
        "properties": properties
    }
    return jsonify(my_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)