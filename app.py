from flask import Flask, render_template, redirect, url_for, request

global app
app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    return render_template("main_order.html")

@app.route("/order", methods = ['GET', 'POST']) 
def index():
    return render_template("main_order.html")

@app.route("/other", methods=['GET', 'POST'])
def other():
    return render_template("other.html")

if __name__ == "__main__":
    app.run(debug="true") 