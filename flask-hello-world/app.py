# Flask hello world

# import flask from flask package
from flask import Flask

# create application object
app = Flask(__name__)

# error handling
app.config['DEBUG'] = True

# use the decorator pattern to
# link the view function to a url
@app.route('/')
@app.route('/hello')
def hello_world():
    return "Hello, World!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route('/name/<name>')
def index(name):
    if name.lower() == 'micheal':
        return 'Hello, {}'.format(name), 200
    else:
        return 'Not Found', 404

# start the development server using the run() method
if __name__ == '__main__':
    app.run()
