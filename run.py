from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/addition', methods=['GET', 'POST'])
def addition():
    if request.method == "POST" :
        num1=request.form['num1']
        num2=request.form['num2']
        result=int(num1)+int(num2)
        return render_template("addition.html", result=result)
    return render_template("addition.html")

@app.route('/subtraction', methods=['GET', 'POST'])
def subtraction():
    if request.method == "POST" :
        num1=request.form['num1']
        num2=request.form['num2']
        result=int(num1)-int(num2)
        return render_template("sub.html", result=result)
    return render_template("sub.html")


if __name__ == '__main__':
    app.run(debug=True)


