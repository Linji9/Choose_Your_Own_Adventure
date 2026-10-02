from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)


@app.route("/template")
def home():
    return render_template("template.html")

@app.route("/hello")
def hello():
    return "Hello, world!"

@app.route("/getCharScene/<char>/<scene>")
def getCharScene(char, scene):
    # go into json file
    with app.open_resource("story.json") as f:
        story_data = json.load(f)
    # get the char
    character = story_data[char]
    # dive in further and get the json file associated with scene 
    scenario = character[scene]
    thatJSONfile = jsonify(scenario)
    return thatJSONfile
