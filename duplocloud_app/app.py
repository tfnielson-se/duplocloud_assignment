from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello", methods=['GET'])
def greeting_message():
    return "Hello, Welcome to my Python-Flask App for DuploCloud"

# /calculate?operation=xyz&x=xx&y=yy
@app.route('/calculate', methods=['GET'])
def calculate():
    operation = request.args.get('operation', type=str)
    x = request.args.get('x', type=float)
    y = request.args.get('y', type=float)

    if operation == 'add':
        result = x + y
    elif operation == 'subtract':
        result = x - y
    elif operation == 'multiply':
        result = x * y
    elif operation == 'divide':
        result = x / y
    else:
        return "Invalid operation or Missing parameters, please check your query value matches format: /calculate?operation=operation_name&x=x_value&y=y_value - example: /calculate?operation=divide&x=10&y=5"

    return f'{operation} x={x} y={y}, result={result}'

@app.route('/reverse-string', methods=['POST'])
def reverse_string():
    data = request.get_json()
    result = []

    for key, value in data.items():
        if isinstance(value, str):
            result.append(value[::-1])

    return result