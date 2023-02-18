from flask import Flask, jsonify
import hashlib
import math

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/md5/<md5_input>")
def md5_hash(md5_input):
    encoded_input = hashlib.md5(md5_input.encode()) #encodes the str, then turns it into md5 form
    return jsonify( #jsonify returns the json input/output format
        input = md5_input,
        output = encoded_input.hexdigest() #converts the md5 format into hexadecimal
    )

@app.route("/factorial/<int:factorial_input>")
def factorial(factorial_input):
    if factorial_input >= 0:
        return jsonify(
            input = factorial_input,
            output = str(math.factorial(factorial_input))
        )
    else:
        return "Please input a positive integer"

@app.route("/fibonacci/<int:fibonacci_input>")
def fibonacci(fibonacci_input):
    fibo_list = []
    n1, n2 = 0, 1
    if fibonacci_input > 1:
        while n1 < fibonacci_input: #while loop that calculates up until the user input
            if n1 > fibonacci_input: #checks if the most recent fibo value is greater than input to stop running and not add to the output list
                break
            else:
                fibo_list.append(n1) #adds most recent fibo value if it is less than user input
            nth = n1 + n2 #fibonacci sequence is adding 2 previous numbers
            n1 = n2 #redefining the number that is 2 spaces away
            n2 = nth #refining the number that is 1 space away
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
        return "Please input a positive integer"

if __name__ == '__main__':
    app.run(port=4000, debug = True) #makes the flask app run on port 4000
