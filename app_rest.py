import uuid

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False


def get_name():
    return 'Контроль потребления электричества'


def get_info():
    return '5 дней подряд расход электричества не выше среднего'


def get_cash():
    return '0'


@app.route('/pushRecommendation', methods=['GET', 'POST'])
def push_recommendation():
    random_uuid = str(uuid.uuid4())
    string = {"id": random_uuid, "name": get_name(), "info": get_info(), "cash": get_cash()}
    return jsonify(string)


if __name__ == '__main__':
    app.run(debug=True, host='192.168.43.150')
    # app.run(debug=True, host='127.0.0.1')
