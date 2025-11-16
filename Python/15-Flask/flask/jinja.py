# Building url dynamically
# Variable Rules
# Jinja 2 Template Engine

# jinja2 Template Engine
'''
=> {{ variable }} expression to print the value of a variable in html.
=> {% ... %} conditional statements and loops.
=> {# ... #} this is fr comments in jinja2 templates.
'''

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

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"<h1>Hello, {name}!</h1>"
    return render_template('form.html')

# Variable rule
@app.route('/success/<score>')
def success(score):
    res = ''
    if int(score) >= 50:
        res = "You have passed the exam!"
    else:
        res = "You have failed the exam."
    return render_template('result.html', result=res)

@app.route('/successres/<int:score>')
def successres(score):
    res = ''
    if int(score) >= 50:
        res = "You have passed the exam!"
    else:
        res = "You have failed the exam."
    exp = {'score': score, 'result': res}
    return render_template('result1.html', result=exp)

# Run the application
if __name__ == "__main__":
    app.run(debug=True) # debug=True enables auto-reload and better error messages