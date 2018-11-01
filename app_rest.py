import os
import json
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


def getRecommendationsJsonName():
    return 'resources/recommendations.json'


def createRecommendations(jsonStr):
    encoder = json.JSONEncoder()
    with open(getRecommendationsJsonName(), 'w') as recJsonFile:
        recJsonFile.write(encoder.encode(jsonStr))
        return recJsonFile


@app.route('/home/v1.0/recommendations')
def get_motions():
    jsonRecommendations = createRecommendations({"foo": ["bar", "baz"]})
    return 'TODO'

@app.route('/getRecommendations',methods=['GET','POST'])
def getJson():
    with open(getRecommendationsJsonName(), "r") as blog_file:
        data = json.load(blog_file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
