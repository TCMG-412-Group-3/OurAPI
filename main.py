from flask import Flask, jsonify
import hashlib
import math
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"


#error handling when md5 input is empty
@app.route("/md5/")
def md5():
    #return HTTP 400 error
    return jsonify(
        input = "",
        output = "No input detected. Please input a string to be hashed"
    ), 404

@app.route("/md5/<md5_input>")
def md5_hash(md5_input):
    #if the input is not a string, return HTTP 400 error
    if not isinstance(md5_input, str):
        return jsonify(
            input = md5_input,
            output = "Input is not a string. Please input a string to be hashed"
        ), 400
    encoded_input = hashlib.md5(md5_input.encode()) #encodes the str, then turns it into md5 form
    return jsonify( #jsonify returns the json input/output format
        input = md5_input,
        output = encoded_input.hexdigest() #converts the md5 format into hexadecimal
    )

@app.route("/factorial/")
def factorialindex():
     return jsonify(
        input = "",
        output = "No input detected. Please input a string to be hashed"
    ), 404

@app.route("/factorial/<factorial_input>")
def factorial(factorial_input):
    try:
        factorial_input = int(factorial_input)
    except ValueError:
        return jsonify(
            input = factorial_input,
            output = "Input is not a valid integer. Please input a valid integer"
        ), 400
    if factorial_input >= 0:
        return jsonify(
            input = factorial_input,
            output = str(math.factorial(factorial_input))
        )
    else:
        return jsonify(
            input = factorial_input,
            output = "Input is a negative number. Please input a positive integer"
        ), 400


@app.route("/fibonacci/")
def fibonacciindex():
        return jsonify(
            input = "",
            output = "Please input a positive integer"
        ), 404

@app.route("/fibonacci/<fibonacci_input>")
def fibonacci(fibonacci_input):
    fibo_list = []
    n1, n2 = 0, 1
    try:
        fibonacci_input = int(fibonacci_input)
    except ValueError:
        return jsonify(
            input = fibonacci_input,
            output = "Input is not a valid integer. Please input a valid integer"
        ), 400
    if fibonacci_input > 1:
        while n1 < fibonacci_input: #while loop that calculates up until the user input
            if n1 > fibonacci_input: #checks if the most recent fibo value is greater than input to stop running and not add to the output list
                break
            else:
                fibo_list.append(n1) #adds most recent fibo value if it is less than user input
            nth = n1 + n2 #fibonacci sequence is adding 2 previous numbers
            n1 = n2 #redefining the number that is 2 spaces away
            n2 = nth #refining the number that is 1 spacee awayy
        return jsonify(
            input = fibonacci_input,
            output = fibo_list
        )
    elif fibonacci_input == 1 or fibonacci_input == 0:
        return jsonify(
            input = fibonacci_input,
            output = [1]
        )
    else:
        return jsonify(
            input = fibonacci_input,
            output = "Input is a negative number. Please input a positive integer"
        ), 400

@app.route("/is-prime/")
def isprimeindex():
    return jsonify(
        input = "",
        output = "Please input a valid positive integer"
    ), 404

@app.route("/is-prime/<isprime_input>")
def isprime(isprime_input):
    try:
        isprime_input = int(isprime_input)
    except ValueError:
        return jsonify(
            input = isprime_input,
            output = "Input is not a valid integer. Please input a valid integer"
        ), 400
    result = True
    if isprime_input < 0:
        return jsonify(
            input = isprime_input,
            output = "Input is a negative number. Please input a positive integer"
        ), 400
    elif isprime_input == 1:
        result = True
    elif isprime_input > 1:
        for i in range(2, isprime_input):
            if (isprime_input % i == 0):
                result = False
                break
            else:
                continue
    return jsonify(
        input = isprime_input,
        output = result
    )


#slack alert with no input string
@app.route("/slack-alert/")
def slack_alertindex():
    return jsonify(
        input = "",
        output = False
    ), 400

#slack alert
@app.route("/slack-alert/<message>")
def slack_alert(message):
#Make a POST request to the Slack webhook URL
    response = requests.post(
        url = "https://hooks.slack.com/services/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",
        json = {"text": message}
    ), 404
    #check if the request was successful, return boolean value
    if response.status_code == 200:
        return jsonify(
            input = message,
            output = True
        )
    else:
        return jsonify(
            input = message,
            output = False
        ), 400
# @app.errorhandler(404)
# def page_not_found(e):
#     return jsonify(
#         error = "404",
#         text = "Not Found"
#     ), 404

if __name__ == '__main__':
    app.run(port=4000, debug = True) #makes the flask app run on port 4000
