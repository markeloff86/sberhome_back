from flask import Flask
from flask_cors import CORS
import json

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


if __name__ == '__main__':
    app.run(debug=True, host='192.168.43.150')
