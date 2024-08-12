#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'


@app.route('/count/<int:parameter>')
def count(parameter):
     # Generate the numbers in the range
    numbers = range(parameter)
    print (numbers)
    
    # Create a string with each number on a separate line
    numbers_str = "\n".join(str(num) for num in numbers) + "\n"


    return numbers_str

        

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return f'{num1 + num2}'
    elif operation == '-':
        return f'{num1 - num2}'
    elif operation == '*':
        return f'{num1 * num2}'
    elif operation == 'div':
        return f'{num1 / num2}'
    elif operation == '%':
        return f'{num1 % num2}'
    else:
        return 'Invalid operation'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
