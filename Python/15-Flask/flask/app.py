from flask import Flask

'''
It create an instance of the Flask class,
which will be your WSGI(Web Server Gateway Interface) application.
'''

# WSGI application
app = Flask(__name__)


# Create a basic route
@app.route('/')
def welcome():
    return "Welcome to Flask, your WSGI application!"

@app.route('/index')
def index():
    return "This is the index page."

# Run the application
if __name__ == "__main__":
    app.run(debug=True) # debug=True enables auto-reload and better error messages