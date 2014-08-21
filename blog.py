#this is the controlling script



# imports
from flask import Flask, render_template, request, session, \
                flash, redirect, url_for, g
import sqlite3


# configurations
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'

app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)


#write a function for connecting to database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
                request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Try again/cheating.'
        else:
            session['logged_in'] = True
            return redirect(url_for('main')) 
    return render_template('login.html', error = error)  

# NOTES ON ABOVE
#method: url_for returns url for function.    url_for('login')    >>>   /
#method: auto_render('login.html')  renders "template.html" in 'templates' dir first



@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)


