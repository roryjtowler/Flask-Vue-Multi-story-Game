from flask import Flask, jsonify, render_template, request, redirect
from flask_cors import CORS
import ast


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

master_story_dict = {}

# generate a ID for new child story
def generateChildID():
    dict_length = str(len(master_story_dict) + 1)
    return dict_length

# add a story as a parent story and add as a child to its corresponding parent story
def addStory(currentID, sentence, positon):

    childID = generateChildID()
    childDict = {"sentence": sentence, "childID": childID}
    master_story_dict[childID] = {"middle": childDict, "top": None, "right": None, "bottom": None, "left": None, "parentID": currentID }
    master_story_dict[currentID][positon] = childDict

@app.route('/createStory', methods=['POST'])
def createStory():

    childID = generateChildID()
    post_data = request.get_json()
    sentence = str(post_data.get("sentence"))
    positon = str(post_data.get("positon"))
    currentID = str(post_data.get("currentID"))


    addStory(currentID, sentence, positon)

    response_object = {
        'id': childID,
        'pos': positon,
        'parentID': currentID,
    }
    return jsonify(response_object)

@app.route('/getStory', methods=['POST'])
def getStory():

    post_data = request.get_json()
    currentID = post_data.get('id')

    if(currentID == "0"):
        master_story_dict.clear();
        currentID = "1"

    response_object = {

            'currentID': currentID,
            'parentID': findParentID(currentID),
            'middle': findInfo(currentID, "middle", "sentence"),
            'top': findInfo(currentID, "top", "sentence"),
            'topID': findInfo(currentID, "top", "childID"),
            'right': findInfo(currentID, "right", "sentence"),
            'rightID': findInfo(currentID, "right", "childID"),
            'bottom': findInfo(currentID, "bottom", "sentence"),
            'bottomID': findInfo(currentID, "bottom", "childID"),
            'left': findInfo(currentID, "left", "sentence"),
            'leftID': findInfo(currentID, "left", "childID"),
    }

    return jsonify(response_object)

# find a child sentence given its parentID and position
def findInfo(currentID, pos, type):

    print(bool(master_story_dict) != False)
    if(bool(master_story_dict) != False):
        storyToRender = master_story_dict.get(currentID)
        if(storyToRender.get(pos) != None):
            sentence = storyToRender.get(pos)
            return sentence.get(type)
        else:
            return ""
    else:
        return ""

# find the parentID of a child (used for going back)
def findParentID(currentID):
    if(bool(master_story_dict) != False):
        storyToRender = master_story_dict.get(currentID)
        if(storyToRender.get("parentID") != None):
            parentID = storyToRender.get("parentID")
            return parentID
        else:
            return ""
    else:
        return ""


if __name__ == '__main__':
    app.run(debug = True)
