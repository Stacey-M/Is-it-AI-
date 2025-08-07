from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start")
def start():
    return render_template("start.html")

@app.route("/G1")
def G1():
    return render_template("G1.html", Img1 = "Ai1.avif", Img2 = "ai2.jpg")

@app.route("/win1")
def win1():
    return render_template("win1.html")

@app.route("/lost1")
def lost1():
    return render_template("lost1.html")

@app.route("/G2")
def G2():
    return render_template("G2.html")

@app.route("/win2")
def win2():
    return render_template("win2.html")

@app.route("/lost2")
def lost2():
    return render_template("lost2.html")

@app.route("/G3")
def G3():
    return render_template("G3.html")

@app.route("/win3")
def win3():
    return render_template("win3.html")

@app.route("/lost3")
def lost3():
    return render_template("lost3.html")

# main driver function
if __name__ == '__main__':
    app.run(debug=True)