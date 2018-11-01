# -*- coding: utf-8 -*-

import random
import uuid
import db_helper as db

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False


# Заглушки. Эмулириют СБОЛ, возвращают название копилки, описание и кол-во денег
def get_name():
    return ['Контроль потребления электричества', 'Ограничение ночного холодильника']


def get_info():
    return ['Потребление электричества выше среднего, откладываем на оплату',
            'Холодильник был открыт во время запрета, откладываем на тренировки']


def get_cash():
    return [200, 100]


@app.route('/pushNotification', methods=['GET', 'POST'])
def push_notification():
    random_uuid = str(uuid.uuid4())
    random_id = random.randint(0, len(get_name()) - 1)
    notification = {
        "id": random_uuid,
        "name": get_name()[random_id],
        "info": get_info()[random_id],
        "cash": str(get_cash()[random_id]) + ' ₽'
    }
    return jsonify(notification=notification)


@app.route('/getMoneyBoxes', methods=['GET', 'POST'])
def get_cli_commands():
    try:
        boxes_list = []
        for i in (0, len(get_name()) - 1):
            emp_dict = {
                'name': get_name()[i],
                'cash': str(get_cash()[i]) + ' ₽'
            }
            boxes_list.append(emp_dict)
    except:
        return "Ошибка получения списка умных копилок"
    return jsonify(smart_box=boxes_list)


@app.route('/checkDate', methods=['GET', 'POST'])
def date_compare():
    time_one = db.select_challenges("last_update_time")
    time_two = db.select_challenges("fail_time")
    return "last_update_time - " + time_two + " | exception time - " + time_one


if __name__ == '__main__':
    app.run(debug=True, host='192.168.43.150')
    # app.run(debug=True, host='127.0.0.1')
