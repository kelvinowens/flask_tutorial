from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    myValue = 12345
    myText = 'Bob is a palendrome.'
    myList = [10, 20, 30, 40, 50]
    return render_template('index.html', myValue=myValue, myText=myText, myList=myList)


@app.route('/test')
def test():
    some_text = 'Hello World'
    return render_template('test.html', some_text=some_text)

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('test'))


@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def repeat(s, times=2):
    return s * times

@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    