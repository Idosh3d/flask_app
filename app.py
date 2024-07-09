from flask import Flask
#app = Flask(__name__)
app = Flask(__name__, static_url_path='')

@app.route('/')
def hello_world():
    return 'Hello, World!'
