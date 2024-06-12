from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World!</h1> <p>How are you?</p>"

@app.route('/hello/')
def hello():
    return "Hello World!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}."

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    number3 = number1 + number2
    return f"{number1} + {number2} = {number3}"

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f'{greeting}, {name}!'
    else:
        return 'Some parameters are missing.'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)