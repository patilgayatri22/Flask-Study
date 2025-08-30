from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
@app.route('/index/<name>')
def hello(name):
    return '<h1>Hello, %s!</h1>' % name
if name == ' main':
    app.run(debug = True)