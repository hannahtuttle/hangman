from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return 'Hello {}!'.format(name)

@app.route('/<last_name>')
def hello_last_name(name):
    return "Hello {}!".format(last_name)

if __name__ == '__main__':
    app.run() 
