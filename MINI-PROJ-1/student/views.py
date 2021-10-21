from flask import Flask
from flask.templating import render_template
app = Flask(__name__)


# Refer to https://flask.palletsprojects.com/en/2.0.x/quickstart/

@app.route('/')
def index():
    return render_template("your_code.html")
    # Your code here

@app.route('/about_me')
def route1func():
    return render_template("about_me.html")

@app.route('/route2')
def route2func():
    return render_template("route2wip.html")

if __name__ == "__main__":
    app.run(debug=True)