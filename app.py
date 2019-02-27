from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/AdminLogin")
def AdminLogin():
    return render_template("adminlogin.html")


@app.route("/AdminPage")
def AdminPage():
    return render_template("MainAdminPage.html")


@app.route("/StaffLogin")
def StaffLogin():
    return render_template("stafflogin.html")


@app.route("/StaffPage")
def StaffPage():
    return render_template("staffpage.html")


@app.route("/StudentLogin")
def StudentLogin():
    return render_template("studentlogin.html")


@app.route("/addition")
def add(a=10, b=20):
    d = a + b
    return render_template("first.html", display=d)


@app.route("/webform")
def display():
    show = "flask jinji webform"
    return render_template("first.html", display=show)


@app.route("/fileinput")
def input():
    return render_template("fileinput.html")


@app.route('/filewriting', methods=['POST', 'GET'])
def filewrite():
    a = request.form["i1"]
    b = request.form["i2"]
    c = request.form["i3"]
    print(a)
    print(b)
    print(c)
    x = open("index.txt", "a")
    x.write("My Name is:" + a + "\nMy Number is:" + b + "\nMy Email is:" + c + "\n")
    x.close()
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug="True")