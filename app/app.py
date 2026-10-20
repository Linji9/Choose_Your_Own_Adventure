from flask import Flask, render_template, jsonify, request
import json


app = Flask(__name__)


@app.route("/template")
def home():
    return render_template("template.html")

@app.route("/hello")
def hello():
    return "Hello, world!"

# for template
@app.route("/scene/<char>/<scene>")
def get_SceneData(char, scene):

    with open("db/story.json", "r") as f:
        story = json.load(f)
    # get the char
    FullCharStory = story[char]
    # dive in further and get the json file associated with scene 
    ActiveScenario = FullCharStory[scene]

    return render_template("scene.html", char = char, sceneData = ActiveScenario)


# for ajax
@app.route("/play")
def getCharScene():
    char = request.args.get("c", default = "princess")
    scene = request.args.get("s", default = "1")
    # go into json, find that key (text choice), return value
    #then everything below here works as normal
    # go into json file, loading json as dict
    with open("db/story.json", "r") as f:
        story = json.load(f)
    # get the char
    character = story[char]
    # dive in further and get the json file associated with scene 
    scenario = character[scene]
    
    thatJSONfile = jsonify(scenario)
    return thatJSONfile