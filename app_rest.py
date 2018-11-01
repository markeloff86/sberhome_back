import random
import uuid

from flask import Flask, jsonify, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False


def get_name():
    return ['Контроль потребления электричества', 'Ограничение ночного холодильника']


def get_info():
    return ['5 дней подряд расход электричества не выше среднего',
            '4 дня подряд без открывния холодильника после ограниченного времени']


def get_cash():
    return ['0','100']


@app.route('/pushNotification', methods=['GET', 'POST'])
def push_notification():
    random_uuid = str(uuid.uuid4())
    random_id = random.randint(0, len(get_name())-1)
    notification = {"id": random_uuid, "name": get_name()[random_id], "info": get_info()[random_id], "cash": get_cash()[random_id]}
    return jsonify(notification=notification)


@app.route('/getMoneyBoxes', methods=['GET', 'POST'])
def get_cli_commands():
    try:
        boxes_list = []
        for i in (0, len(get_name()) - 1):
            empDict = {
                'name': get_name()[i],
                'cash': get_cash()[i],
                'info': get_info()[i]}
            boxes_list.append(empDict)
    except:
        return "Error read JSON"
    return jsonify(smart_box=boxes_list)


if __name__ == '__main__':
    # app.run(debug=True, host='192.168.43.150')
    app.run(debug=True, host='127.0.0.1')
