from pexpect import pxssh
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route("/home")
def home():
    return render_template("index.html")

"""@app.route("/home", methods=['POST'])
def homePost():
    text = request.form['nm']
    processed_text = text.upper()
    ssh = pxssh.pxssh()
    #("host", "user", "password")
    ssh.login("10.4.2.41", "icsserver", "password")
    ssh.sendline("touch " + str(processed_text) + ".txt")
    return render_template("index.html", variable=processed_text)
"""
if __name__ == "__main__":
    app.run()
