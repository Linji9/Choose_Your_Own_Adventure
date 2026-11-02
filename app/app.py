from flask import Flask, render_template, jsonify, request
import json


app = Flask(__name__)

# for template
@app.route("/scene/<char>/<scene>")
def get_scene_data(char, scene):

    with open("db/story.json", "r") as f:
        story = json.load(f)

    # json file is structured so that if the scene is the ending, 
    # it's text as opposed to "3.2"

    # is the scene a number (middle scene) or text (an ending)
    try:
        # is a number/middle scene
        float(scene)
        is_ending = False
    except (ValueError, TypeError):
        # is text/an ending
        is_ending = True

    if not is_ending:
        # get the char's story within bigger json file
        full_char_story = story[char]
        # only get data associated with scene 
        active_scenario = full_char_story[scene]
        return render_template("scene.html", char = char, sceneData = active_scenario)
    
    else:
        all_endings = story["endings"]
        active_scenario = all_endings[scene]
        return render_template("ending.html", sceneData = active_scenario)


# OBSOLETE 

# for ajax
@app.route("/play")
def getCharScene():
    char = request.args.get("c", default = "princess")
    scene = request.args.get("s", default = "1")

    with open("db/story.json", "r") as f:
        story = json.load(f)
    # get data for char
    character = story[char]
    # get the data associated with scene 
    scenario = character[scene]
    
    scene_json = jsonify(scenario)
    return scene_json

# part of template, for testing purposes
@app.route("/template")
def home():
    return render_template("template.html")

# part of template, for practice purposes
@app.route("/hello")
def hello():
    return "Hello, world!"