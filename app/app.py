from flask import Flask, render_template

app = Flask(__name__)


@app.route("/template")
def home():
    return render_template("template.html")

@app.route("/hello")
def hello():
    return "Hello, world!"

@app.route("/getCharScene/<char><scene>")
def getCharScene(char, scene):
    # go into json file
    # get the char
    # dive in further and get the json file associated with scene 
    thatJSONfile = None
    return thatJSONfile