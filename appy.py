from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)



# main driver function
if __name__ == '__main__':
    app.run(debug=True)