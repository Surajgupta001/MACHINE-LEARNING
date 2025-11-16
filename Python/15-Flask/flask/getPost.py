from flask import Flask, render_template, request

'''
It create an instance of the Flask class,
which will be your WSGI(Web Server Gateway Interface) application.
'''

# WSGI application
app = Flask(__name__)


# Create a basic route
@app.route('/')
def welcome():
    return "<html><h1>Welcome to Flask, your WSGI application!</h1></html>"

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"<h1>Hello, {name}!</h1>"
    return render_template('form.html')
        

# Run the application
if __name__ == "__main__":
    app.run(debug=True) # debug=True enables auto-reload and better error messages