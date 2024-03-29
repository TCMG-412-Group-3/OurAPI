from flask import Flask, jsonify, request
import hashlib
import math
import requests
import redis

app = Flask(__name__)
r = redis.Redis(host='redis-server')

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
    # if not isinstance(md5_input, str):
    #     return jsonify(
    #         input = md5_input,
    #         output = "Input is not a string. Please input a string to be hashed"
    #     ), 400
    encoded_input = hashlib.md5(md5_input.encode()) #encodes the str, then turns it into md5 form
    return jsonify( #jsonify returns the json input/output format
        input = md5_input,
        output = encoded_input.hexdigest() #converts the md5 format into hexadecimal
    )

@app.route("/factorial/")
def factorialindex():
     return jsonify(
        input = "",
        output = "No input detected. Please input a number to be factorialized"
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
            output = (math.factorial(factorial_input))
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
        while n1 <= fibonacci_input: #while loop that calculates up until the user input
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
    elif fibonacci_input == 1:
        return jsonify(
            input = fibonacci_input,
            output = [0,1,1]
        )
    elif fibonacci_input == 0:
        return jsonify(
            input = fibonacci_input,
            output = [0]
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
        result = False
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
#The URL will be given in the #tcmg412-group-3 channel
    response = requests.post(
        url = "INSERT_SLACK_WEBHOOK_URL_HERE",
        json = {"text": message}
    )
    #check if the request is OK (reponse code below 400)
    if response.ok:
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

@app.route("/keyval", methods = ['POST', 'PUT']) #json inputs
def keyvaljson():
    keyval_error = ""

    keyval_data = request.get_json()
    #if keyval_data does not have storage-key or storage-val, return 400
    if 'storage-key' not in keyval_data or 'storage-val' not in keyval_data or not request.get_json():
        keyval_status = 400
        keyval_error = "Invalid Request: Request is empty"
        keyval_command = ''
        keyval_response = jsonify(
            command = keyval_command,
            status = keyval_status,
            error = keyval_error
        )
        return keyval_response, keyval_status

    storage_key = keyval_data['storage-key']
    storage_val = keyval_data['storage-val']

    #If request is empty, return 400
    if request.method == 'POST':
        #if JSON is empty, return 400
        if  keyval_data['storage-key'] == '':
            keyval_status = 400
            keyval_error = "Invalid Request: Request is empty"
        else:    
            if r.exists(storage_key) == False:
                r.set(storage_key, storage_val)
                keyval_status = 200
            elif r.exists(storage_key) == True:
                keyval_status = 409
                keyval_error = "Key already exists"
            else:
                keyval_status = 400
                keyval_error = "Invalid request"
        keyval_command = 'CREATE '+storage_key+'/'+storage_val
        
    elif request.method == 'PUT':
        if keyval_data['storage-key'] == '':
            keyval_status = 400
            keyval_error = "Invalid Request: Request is empty"
        else:    
            if r.exists(storage_key) == True:
                r.delete(storage_key)
                r.set(storage_key, storage_val)
                keyval_status = 200
            elif r.exists(storage_key) == False:
                keyval_status = 404
                keyval_error = 'Key does not exist'
            else:
                keyval_status = 400
                keyval_error = "Invalid Request"
        keyval_command = 'REPLACE VALUE FOR '+storage_key+' WITH '+storage_val

    if keyval_status == 200:
        keyval_result = True
    else:
        keyval_result = False

    return jsonify(
        key = storage_key,
        value = storage_val,
        command = keyval_command,
        result = keyval_result,
        error = keyval_error
    ), keyval_status

@app.route('/keyval/', defaults={'storage_key': ""}, methods = ['GET', 'DELETE'])
@app.route("/keyval/<storage_key>", methods = ['GET', 'DELETE']) #str inputs
def keyvalstr(storage_key):
    keyval_error = ""
    storage_val = ''
    
    if request.method == 'GET':
        if storage_key == "":
            keyval_status = 400
            keyval_error = "Invalid Request: Request is empty"
        else:
            if r.exists(storage_key) == True:
                storage_val = (r.get(storage_key)).decode()
                keyval_status = 200    
            elif r.exists(storage_key) == False:
                keyval_status = 404
                keyval_error = "Key does not exist"
            else:
                keyval_status = 400
                keyval_error = "Invalid request"
        keyval_command = 'GET KEY: '+storage_key

    elif request.method == 'DELETE':
        if storage_key == "":
            keyval_status = 400
            keyval_error = "Invalid Request: Request is empty"
        else:        
            if r.exists(storage_key) == True:
                storage_val = (r.get(storage_key)).decode()
                r.delete(storage_key)
                keyval_status = 200
            elif r.exists(storage_key) == False:
                keyval_status = 404
                keyval_error = "Key does not exist"
            else:
                keyval_status = 400
                keyval_error = "Invalid request"            
        keyval_command = 'DELETE '+storage_key

    if keyval_status == 200:
        keyval_result = True
    else:
        keyval_result = False

    return jsonify(
        key = storage_key,
        value = storage_val,
        command = keyval_command,
        result = keyval_result,
        error = keyval_error
    ), keyval_status
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
