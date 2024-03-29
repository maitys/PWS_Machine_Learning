from flask import Flask
from flask import request

app = Flask(__name__) # creates the Flask instance, __name__ is the name of the current Python module

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/hello1")
def hello_world1():
    return "Hello, World!1"

@app.route("/hello2")
def hello_world2():
    return "Hello, World!2"

@app.route('/test_fun') 
def test():
    a = 5+6
    return "this my first fun in flask {}".format(a)

@app.route('/input_url') # http://192.168.4.78:5000/input_url?input_value=siddharth
def request_input():
    data = request.args.get('input_value')
    return "this is my input from url {}".format(data)

if __name__=="__main__": # checks whether this file is executed directly from the Python interpreter, and not used as an imported module
    app.run(host="0.0.0.0") # runs the application on the repl development server