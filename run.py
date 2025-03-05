from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/addition')
def addition():
    return render_template("addition.html")


if __name__ == '__main__':
    app.run(debug=True)


