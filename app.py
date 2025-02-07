## VS Code
##python
##virtual environment
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # http://
def home():
    # return "Welcome to Flask!"
    # return "<h1>Welcome to Flask!</h1>"
    # return render_template('index.html')
    users = ['Afeef Ahmed', 'Sarnali Ahmed', 'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Mostak']
    return render_template('index.html', users=users)

@app.route('/about') # http://
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)