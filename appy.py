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




# main driver function
if __name__ == '__main__':
    app.run(debug=True)