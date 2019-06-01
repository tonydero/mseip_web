# Created on Wed 2019.05.22 17:31 UTC
# by Tony DeRocchis

from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/home/")
def home():
    return render_template('home.html')

@app.route("/research/")
def research():
    return render_template('research.html')

if __name__ == "__main__":
    app.run()
