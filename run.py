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


if __name__ == '__main__':
    app.run(debug=True)


