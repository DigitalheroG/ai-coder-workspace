from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, World! Welcome to Flask!"


@app.route('/<name>')
def hello_name(name):
    return f"Hello, {name}! Welcome to Flask!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)