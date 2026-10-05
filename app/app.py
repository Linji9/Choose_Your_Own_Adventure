from flask import Flask, render_template, jsonify, request
import json


app = Flask(__name__)


@app.route("/template")
def home():
    return render_template("template.html")

@app.route("/hello")
def hello():
    return "Hello, world!"

# @app.route("/getCharScene/<char>/<scene>")
# def getCharScene(char, scene):
#     # go into json file, loading json as dict
#     with open("www/static/assets/story.json", "r") as f:
#         story = json.load(f)
#     # get the char
#     character = story[char]
#     # dive in further and get the json file associated with scene 
#     scenario = character[scene]
#     thatJSONfile = jsonify(scenario)
#     return thatJSONfile

@app.route("/play")
def getCharScene():
    char = request.args.get("c", default = "princess")
    scene = request.args.get("s", default = "1")
    # go into json file, loading json as dict
    with open("www/static/assets/story.json", "r") as f:
        story = json.load(f)
    # get the char
    character = story[char]
    # dive in further and get the json file associated with scene 
    scenario = character[scene]
    
    thatJSONfile = jsonify(scenario)
    return thatJSONfile