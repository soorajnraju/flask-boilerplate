from flask import Flask, redirect, session, render_template, url_for, request
import functools
from db.mysql import MySQL

app = Flask(__name__)
app.secret_key = '8v5Wrw4ZYFCnEb79qVEqOWUN2XCND91m'

def login_required(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("login", next=request.url))
        return func(*args, **kwargs)

    return secure_function

@app.route('/home')
@login_required
def home():
    return render_template('main.html')

@app.route('/')
@app.route('/login')
def login():
    if 'username' in session:
        return redirect("home", code=303)
    session['username']='sooraj'
    return render_template('login.html')
